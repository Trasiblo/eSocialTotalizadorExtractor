
class extracao:
    """
    extrai dados do xml informado
    """    
    def __init__(self, nome_arquivo:str, data_dict) -> None:
        """retorna os dados do xml

        Args:
            nome_arquivo (str): nome do arquivo para extração
            data_dict (_type_): xml em formato dict
        """        
        self.nome_arquivo = nome_arquivo
        self.data_dict = data_dict

    def s5001(self):
        tabela = {}
        tabela['arquivo'] = self.nome_arquivo
        
        #evtBasesTrab
        dados =  self.data_dict['eSocial']['retornoProcessamentoDownload']['evento']['eSocial']
        
        evtBasesTrab = dados['evtBasesTrab']
        dados = evtBasesTrab
        tabela['perApur'] = dados['ideEvento']['perApur'] #referencia pagamento
        tabela['cpfTrab'] = dados['ideTrabalhador']['cpfTrab'] 
        tabela['nrRecArqBase'] = dados['ideEvento']['nrRecArqBase']
    

        try:
            infoCpCalc = dados['infoCpCalc']
            dados = infoCpCalc
            tabela['tpCR'] = dados['tpCR'] 
            tabela['vrCpSeg'] = dados['vrCpSeg'] 
            tabela['vrDescSeg'] = dados['vrDescSeg'] 
        
        
            infoCp = evtBasesTrab['infoCp']
            dados = infoCp
            tabela['nrInsc'] = dados['ideEstabLot']['nrInsc']
            tabela['codLotacao'] = dados['ideEstabLot']['codLotacao']
            
            infoCategIncid = infoCp['ideEstabLot']['infoCategIncid']
            dados = infoCategIncid
            tabela['matricula'] = dados['matricula']
            tabela['codCateg'] = dados['codCateg']


            infoBaseCSs = infoCategIncid['infoBaseCS']

            #inicia com o valor zerado
            tabela['valor_baseInss'] = '0'
            tabela['valor_descInss'] = '0'
            
            """
            Informações sobre bases de cálculo, descontos e deduções de 
            contribuições sociais devidas à Previdência Social e a Outras Entidades e Fundos.
            """
            for infoBaseCS in infoBaseCSs:
                if(infoBaseCS['tpValor'] == '11'): #11 - Base de cálculo da contribuição previdenciária normal
                    tabela['valor_baseInss'] = infoBaseCS['valor'] 
                
                #19 - Base de cálculo da contribuição previdenciária exclusiva do empregado
                
                if(infoBaseCS['tpValor'] == '21'): #21 - Valor total descontado do trabalhador para recolhimento à Previdência Social
                    tabela['valor_descInss'] = infoBaseCS['valor'] 
                
                #32 - Valor pago ao trabalhador a título de salário-maternidade

        #except KeyError as error:  
            #print(error)
        finally:    
            return tabela
    
    
    def s3000(self):
        tabela = {}
        
        #nome do arquivo
        tabela['arquivo'] = self.nome_arquivo
        
        dados =  self.data_dict['eSocial']['retornoProcessamentoDownload']['evento']['eSocial']
        
        
        #evtExclusao 
        evtExclusao = dados['evtExclusao']
        dados = evtExclusao
        tabela['id'] = dados['@Id']
        
        
        #infoExclusao
        infoExclusao = evtExclusao['infoExclusao']
        dados = infoExclusao
        tabela['infoExclusao_tpEvento'] = dados['tpEvento']
        tabela['infoExclusao_nrRecEvt'] = dados['nrRecEvt']
        #   ideTrabalhador
        ideTrabalhador = infoExclusao['ideTrabalhador']
        dados = ideTrabalhador
        tabela['infoExclusao_cpfTrab'] = dados['cpfTrab']
        
        
        if (tabela['infoExclusao_tpEvento'] == 'S-1200'):
            #   ideFolhaPagto
            ideFolhaPagto = infoExclusao['ideFolhaPagto']
            dados = ideFolhaPagto
            tabela['infoExclusao_perApur'] = dados['perApur']
        
                
        
        #retornoEvento 
        dados =  self.data_dict['eSocial']['retornoProcessamentoDownload']['recibo']['eSocial']
        
        retornoEvento = dados['retornoEvento']
        dados = retornoEvento
        
        recibo = retornoEvento['recibo']
        dados = recibo
        tabela['recibo_nrRecibo'] = dados['nrRecibo']
    

        #try:
        #
        #    #inicia com o valor zerado
        #    tabela['valor_baseInss'] = '0'
        #    tabela['valor_descInss'] = '0'
        #    
        #    """
        #    Informações sobre bases de cálculo, descontos e deduções de 
        #    contribuições sociais devidas à Previdência Social e a Outras Entidades e Fundos.
        #    """
        #    for infoBaseCS in infoBaseCSs:
        #        if(infoBaseCS['tpValor'] == '11'): #11 - Base de cálculo da contribuição previdenciária normal
        #            tabela['valor_baseInss'] = infoBaseCS['valor'] 
        #        
        #        #19 - Base de cálculo da contribuição previdenciária exclusiva do empregado
        #        
        #        if(infoBaseCS['tpValor'] == '21'): #21 - Valor total descontado do trabalhador para recolhimento à Previdência Social
        #            tabela['valor_descInss'] = infoBaseCS['valor'] 
        #        
        #        #32 - Valor pago ao trabalhador a título de salário-maternidade
        #
        #except KeyError as error:  
        #    print(error)

        return tabela