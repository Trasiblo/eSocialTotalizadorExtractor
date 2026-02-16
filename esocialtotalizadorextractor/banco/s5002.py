import sqlite3

from esocialtotalizadorextractor.banco import conn

def criar_tabela():
    """ cria a tabela 'tarefa' caso ela não exista """
    conn.execute("""
    create table if not exists s5002 (
        --id text primary key,
        arquivo text,
        nrRecArqBase text,
        perApur text,
        cpfBenef text,
        vlrRendTrib float,
        vlrRendTrib13 float,
        vlrPrevOficial float,
        vlrPrevOficial13 float,
        vlrCRMen float,
        vlrCR13Men float,
        vlrParcIsenta65 float,
        vlrParcIsenta65Dec float,
        vlrDiarias float,
        vlrAjudaCusto float,
        vlrIndResContrato float,
        vlrAbonoPec float,
        vlrRendMoleGrave float,
        vlrRendMoleGrave13 float,
        vlrAuxMoradia float,
        vlrBolsaMedico float,
        vlrBolsaMedico13 float,
        vlrJurosMora float,
        vlrIsenOutros float
    )
    """)    


def add(dados:dict):
    """ adiciona uma nova tarefa """
    
    colunas = ', '.join(dados.keys()) #lista de colunas separadas por virgula
    curingas = ', '.join('?' * len(dados)) #quantidade de parametros ? separados por virgulas
    
    sql = 'INSERT INTO s5002 ({}) VALUES ({})'.format(colunas, curingas)
    valores = [int(x) if isinstance(x, bool) else x for x in dados.values()]
    
    conn.execute(sql, valores)
    conn.commit()

def limpar_registros():
    """ exclui todos os registros da tabala s5002 """
    conn.execute("delete from s5002")
    conn.commit()