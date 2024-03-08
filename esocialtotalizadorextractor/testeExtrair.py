from tqdm import tqdm
from utilitarios import *
import extracao
import esocialtotalizadorextractor.banco.s5001
import esocialtotalizadorextractor.banco.s3000



#informar nome da pasta com os xmls de retorno da Consulta Processamento de Lote
diretorio = '/home/tasso/Projects/esocial/pyTotalizadores/' + '3678466'
#diretorio = "I:\\USUARIO\\Área de Trabalho\\2024\\2024-ESOCIAL\\2024-ERROS_TEMPOS_ASPEC\\3678466"
#diretorio = "I:\\USUARIO\\Área de Trabalho\\2024\\2024-ESOCIAL\\2024-ERROS_TEMPOS_ASPEC\\2024"

#dados S-5001
pasta = listarArquivos(diretorio)
barra = tqdm(total=len(pasta), desc='S-5001', unit='arq')
esocialtotalizadorextractor.banco.s5001.criar_tabela()
esocialtotalizadorextractor.banco.s5001.limpar_registros()

for arquivo in pasta:
    nome_arquivo = arquivo
    data_dict = carregarXml(nome_arquivo)
    #print(nome_arquivo)
    
    extrai = extracao.extracao(nome_arquivo, data_dict)

    tabela = extrai.s5001()
    
    esocialtotalizadorextractor.banco.s5001.add(tabela)
    barra.update()
    
#dados S-3000  
pasta = listarArquivos(diretorio, 'S-3000')
barra = tqdm(total=len(pasta), desc='S-3000', unit='arq')
esocialtotalizadorextractor.banco.s3000.criar_tabela()
esocialtotalizadorextractor.banco.s3000.limpar_registros()

for arquivo in pasta:
    nome_arquivo = arquivo
    data_dict = carregarXml(nome_arquivo)
    
    extrai = extracao.extracao(nome_arquivo, data_dict)

    tabela = extrai.s3000()
    
    esocialtotalizadorextractor.banco.s3000.add(tabela)
    barra.update()

