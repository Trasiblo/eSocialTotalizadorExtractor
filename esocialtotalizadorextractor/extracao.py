
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
    
    def s5002(self):
        tabela = {}
        tabela['arquivo'] = self.nome_arquivo

        #divise o nome do arquivo e pega só o nome do arquivo
        nome_arquivo = self.nome_arquivo.split("\\")[-1]
        inicial_arquivo = nome_arquivo[:2]
        
        #evtBasesTrab
        #verificar se o arquivo inica 
        #ID (bem do downlaod) ou eSocial_EventoRecibo (manual)
        if (inicial_arquivo == 'ID'):
            dados =  self.data_dict['eSocial']['retornoProcessamentoDownload']['evento']['eSocial']
        
        if (inicial_arquivo == 'eS'):
            dados =  self.data_dict['eSocial']['retornoEventoCompleto']['evento']['eSocial']
        
        evtIrrfBenef = dados['evtIrrfBenef']
        dados = evtIrrfBenef
        tabela['perApur'] = dados['ideEvento']['perApur'] #referencia pagamento
        tabela['cpfBenef'] = dados['ideTrabalhador']['cpfBenef'] 
        tabela['nrRecArqBase'] = dados['ideEvento']['nrRecArqBase']
    

        try:
            ideTrabalhador = dados['ideTrabalhador']
            dados = ideTrabalhador

            totInfoIR = dados['totInfoIR']['consolidApurMen']
            dados = totInfoIR
            tabela['vlrRendTrib'] = dados['vlrRendTrib'] 
            tabela['vlrRendTrib13'] = dados['vlrRendTrib13'] 
            tabela['vlrPrevOficial'] = dados['vlrPrevOficial'] 
            tabela['vlrPrevOficial13'] = dados['vlrPrevOficial13'] 
            tabela['vlrCRMen'] = dados['vlrCRMen'] 
            tabela['vlrCR13Men'] = dados['vlrCR13Men']
            tabela['vlrParcIsenta65'] = dados['vlrParcIsenta65'] 
            tabela['vlrParcIsenta65Dec'] = dados['vlrParcIsenta65Dec'] 
            tabela['vlrDiarias'] = dados['vlrDiarias'] 
            tabela['vlrAjudaCusto'] = dados['vlrAjudaCusto']
            tabela['vlrIndResContrato'] = dados['vlrIndResContrato'] 
            tabela['vlrAbonoPec'] = dados['vlrAbonoPec'] 
            tabela['vlrRendMoleGrave'] = dados['vlrRendMoleGrave']
            tabela['vlrRendMoleGrave13'] = dados['vlrRendMoleGrave13'] 
            tabela['vlrAuxMoradia'] = dados['vlrAuxMoradia'] 
            tabela['vlrBolsaMedico'] = dados['vlrBolsaMedico'] 
            tabela['vlrBolsaMedico13'] = dados['vlrBolsaMedico13'] 
            tabela['vlrJurosMora'] = dados['vlrJurosMora'] 
            tabela['vlrIsenOutros'] = dados['vlrIsenOutros'] 
           
          
        #except KeyError as error:  
            #print(error)
        finally:    
            return tabela
    
    def s3000(self, tpEvento = 'S-1200'):
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
        
        
        if (tabela['infoExclusao_tpEvento'] == tpEvento):
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

        return tabela