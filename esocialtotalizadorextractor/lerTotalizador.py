from tqdm import tqdm
import esocialtotalizadorextractor.utilitarios
import esocialtotalizadorextractor.extracao
import esocialtotalizadorextractor.banco.s5001
import esocialtotalizadorextractor.banco.s3000
import esocialtotalizadorextractor.banco.s5002


#diretorio = '/home/tasso/Projects/esocial/pyTotalizadores/' + '3678466'
class lerXml:
    def __init__(self, diretorio:str):
        """recebe o diretorio onde esta os xmls

        Args:
            diretorio (str): local onde esta armazenado os xmls
            ex: diretorio = '/home/tasso/Projects/esocial/pyTotalizadores/' + '3678466'
        """
        self.diretorio = diretorio
        self.banco_s5001 = esocialtotalizadorextractor.banco.s5001
        self.banco_s3000 = esocialtotalizadorextractor.banco.s3000
        self.banco_s5002 = esocialtotalizadorextractor.banco.s5002
        self.utilitario = esocialtotalizadorextractor.utilitarios
        self.extracao = esocialtotalizadorextractor.extracao


    def s5001(self):
        self.s3000('S-1200')
        #dados S-5001
        pasta = self.utilitario.listarArquivos(self.diretorio)
        barra = tqdm(total=len(pasta), desc='S-5001', unit='arq')
        self.banco_s5001.criar_tabela()
        self.banco_s5001.limpar_registros()

        for arquivo in pasta:
            nome_arquivo = arquivo
            data_dict = self.utilitario.carregarXml(nome_arquivo)
            
            extrai = self.extracao.extracao(nome_arquivo, data_dict)

            tabela = extrai.s5001()
                        
            self.banco_s5001.add(tabela)
            barra.update()

    def s5002(self):
        self.s3000('S-1210')
        #dados S-5002
        pasta = self.utilitario.listarArquivos(self.diretorio, 'S-5002')
        barra = tqdm(total=len(pasta), desc='S-5002', unit='arq')
        self.banco_s5002.criar_tabela()
        self.banco_s5002.limpar_registros()

        for arquivo in pasta:
            nome_arquivo = arquivo
            data_dict = self.utilitario.carregarXml(nome_arquivo)
            
            extrai = self.extracao.extracao(nome_arquivo, data_dict)

            tabela = extrai.s5002()
                        
            self.banco_s5002.add(tabela)
            barra.update()

    def s3000(self, tpEvento:str):
        #dados S-3000  
        pasta = self.utilitario.listarArquivos(self.diretorio, 'S-3000')
        barra = tqdm(total=len(pasta), desc='S-3000', unit='arq')

        self.banco_s3000.criar_tabela()
        self.banco_s3000.limpar_registros()

        for arquivo in pasta:
            nome_arquivo = arquivo
            data_dict = self.utilitario.carregarXml(nome_arquivo)
            
            extrai = self.extracao.extracao(nome_arquivo, data_dict)

            tabela = extrai.s3000(tpEvento=tpEvento)
            
            self.banco_s3000.add(tabela)
            barra.update()

