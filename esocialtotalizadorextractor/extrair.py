import csv
from utilitarios import *
import extracao

nomeArq = gerarNomeArquivo() + '-Totalizador.csv'
arq = open(nomeArq, "a", newline=None)

arq.write("arquivo;perApur;cpfTrab;tpCR;vrCpSeg;vrDescSeg;nrInsc;codLotacao;matricula;codCateg;valor_baseInss;valor_descInss\n")

#informar nome da pasta com os xmls de retorno da Consulta Processamento de Lote
diretorio = '/home/tasso/Projects/esocial/pyTotalizadores/' + '3678466'
diretorio = "I:\\USUARIO\\Área de Trabalho\\2024\\2024-ESOCIAL\\2024-ERROS_TEMPOS_ASPEC\\3678466"

pasta = listarArquivos(diretorio)


for arquivo in pasta:
    nome_arquivo = arquivo
    data_dict = carregarXml(nome_arquivo)
    print(nome_arquivo)
    
    extrai = extracao.extracao(nome_arquivo, data_dict)

    tabela = extrai.s5001()

    registro = list()
    for campo in tabela:
        registro.append(tabela[campo])


    
    arq1 = csv.writer(arq,delimiter=';')
    arq1.writerow(registro)
