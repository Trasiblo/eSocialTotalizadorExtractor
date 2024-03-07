import os
import datetime
import xmltodict

"""
    retorno lista de arquivos

    pasta: caminho da pasta onde encontra os arquivos
    evento: qual evento sera filtrado por padrao e o S-5001

    Returns:
        _type_: caminho e nome do arquivo
"""
def listarArquivos(pasta:str, evento = 'S-5001'):
    """Lista todos os arquivos de uma determinada pasta

    Args:
        pasta (str): path da pasta a ser presquisada
        evento (str, optional): informa o filtro a ser utilizado. Defaults to 'S-5001'.

    Returns:
        list: lista de arquivos encontratos na determinada pasta
    """    
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    filtrados = [arq for arq in arquivos if arq.lower().endswith( evento.lower() + ".xml")]
    return filtrados

def gerarNomeArquivo():
    """gerar data e hora para formar nome de arquivos

    Returns:
        str: contendo data e hora AAAAMMDD-HHMMSS
    """    
    agora = datetime.datetime.now()
    return agora.strftime("%Y%m%d-%H%M%S")


def carregarXml(nome_arquivo:str):
    """carregar xml em memoria e converter para dict

    Args:
        nome_arquivo (str): path do arquivo

    Returns:
        dict: retorna o xml em dict
    """    
    response = open(nome_arquivo, "r")
    response1 = response.read()

    data_dict = xmltodict.parse(response1)
    return data_dict
