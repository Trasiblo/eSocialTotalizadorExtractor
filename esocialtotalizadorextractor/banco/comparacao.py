import sqlite3

from esocialtotalizadorextractor.banco import conn

def criar_tabela():
    """ cria a tabela 'tarefa' caso ela não exista """
    conn.execute("""
    create table if not exists comparacao (
        arquivo text,
        perApur text,
        cpf text,
        nome text,
        vlrRendTrib float,
        vlrPrevOficial float,
        vlrCRMen float
    )
    """)    


def add(dados:dict):
    """ adiciona uma nova tarefa """
    
    colunas = ', '.join(dados.keys()) #lista de colunas separadas por virgula
    curingas = ', '.join('?' * len(dados)) #quantidade de parametros ? separados por virgulas
    
    sql = 'INSERT INTO comparacao ({}) VALUES ({})'.format(colunas, curingas)
    valores = [int(x) if isinstance(x, bool) else x for x in dados.values()]
    
    conn.execute(sql, valores)
    conn.commit()

def limpar_registros():
    """ exclui todos os registros da tabala comparacao """
    conn.execute("delete from comparacao")
    conn.commit()