import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class relatorio:

    def __init__(self, conn:sqlite3.connect):
        """monta os relatorios baseados nos arquivos já lidos

        Args:
            conn (sqlite3.connect): recebe conexão com a base de dados
        """
        self.conn = conn
        
    

    def get_valor(self):
        sql = """
        with ex as (
        select * from s3000 ex
        where
        ex.infoExclusao_tpEvento = 'S-1200'),

        validos as( 
        select t.* from s5001 t
        left join ex on t.nrRecArqBase = ex.infoExclusao_nrRecEvt and ex.infoExclusao_perApur = t.perApur and ex.infoExclusao_cpfTrab = t.cpfTrab
        where ex.id is null)

        select 
        s.perApur, 
        count(s.perApur),
        sum(s.vrCpSeg),
        sum(s.vrDescSeg),
        sum(valor_baseInss),
        sum(valor_descInss)
        from validos s 
        group by s.perApur
        """

        consulta = self.conn.execute(sql)
        consulta.row_factory = dict_factory
        return consulta.fetchall()

    def get_valor_analitico(self):
        sql = """
        with ex as (
        select * from s3000 ex
        where
        ex.infoExclusao_tpEvento = 'S-1200'),

        validos as( 
        select t.* from s5001 t
        left join ex on t.nrRecArqBase = ex.infoExclusao_nrRecEvt and ex.infoExclusao_perApur = t.perApur and ex.infoExclusao_cpfTrab = t.cpfTrab
        where ex.id is null)

        select 
        s.*
        from validos s 
        """
        consulta = self.conn.execute(sql)
        consulta.row_factory = dict_factory
        return consulta.fetchall()