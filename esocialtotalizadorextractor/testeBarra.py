from tqdm import tqdm
from time import sleep
import csv
from utilitarios import *
import extracao
import esocialtotalizadorextractor.banco.s5001
import esocialtotalizadorextractor.banco.s3000



#informar nome da pasta com os xmls de retorno da Consulta Processamento de Lote
diretorio = '/home/tasso/Projects/esocial/pyTotalizadores/' + '3678466'
diretorio = "I:\\USUARIO\\Área de Trabalho\\2024\\2024-ESOCIAL\\2024-ERROS_TEMPOS_ASPEC\\3678466"
#diretorio = "I:\\USUARIO\\Área de Trabalho\\2024\\2024-ESOCIAL\\2024-ERROS_TEMPOS_ASPEC\\2024"

#dados S-5001
pasta = listarArquivos(diretorio)
#esocialtotalizadorextractor.banco.s5001.criar_tabela()
#esocialtotalizadorextractor.banco.s5001.limpar_registros()
print('importando dados S-5001')
barra = tqdm(range(len(pasta)))
#barra.update()
#barra.update()
#barra.update()

#print(barra)

for arquivo in pasta:
    nome_arquivo = arquivo
    barra.update()
    sleep(0.001)
    
    
    #
    # data_dict = carregarXml(nome_arquivo)
    #print(nome_arquivo)
    
    #extrai = extracao.extracao(nome_arquivo, data_dict)

    #tabela = extrai.s5001()
    
    #esocialtotalizadorextractor.banco.s5001.add(tabela)

#for i in tqdm(range(10000)):
#    sleep(0.001)