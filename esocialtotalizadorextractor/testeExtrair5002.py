import csv
from utilitarios import *
import extracao
import esocialtotalizadorextractor.banco.s5002


#informar nome da pasta com os xmls de retorno da Consulta Processamento de Lote
diretorio = '/home/tasso/Projects/esocial/pyTotalizadores/' + '3678466'
diretorio = "C:\\Users\\rh_t\\Documents\\projetos\\totalizador\\18714655"
#diretorio = "I:\\USUARIO\\Área de Trabalho\\2024\\2024-ESOCIAL\\2024-ERROS_TEMPOS_ASPEC\\2024"

pasta = listarArquivos(diretorio, 'S-5002')

#esocialtotalizadorextractor.banco.s5002.limpar_registros()
esocialtotalizadorextractor.banco.s5002.criar_tabela()
for arquivo in pasta:
    nome_arquivo = arquivo
    data_dict = carregarXml(nome_arquivo)
    print(nome_arquivo)
    
    extrai = extracao.extracao(nome_arquivo, data_dict)

    tabela = extrai.s5002()
    
    esocialtotalizadorextractor.banco.s5002.add(tabela)
    
  
