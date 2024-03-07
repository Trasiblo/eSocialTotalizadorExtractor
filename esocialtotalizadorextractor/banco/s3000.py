import sqlite3

from banco import conn


def criar_tabela():
    """ cria a tabela 's3000' caso ela não exista """
    conn.execute("""
    create table if not exists s3000 (
        id text primary key,
        arquivo text,
        infoExclusao_tpEvento text, 
        infoExclusao_nrRecEvt text,
        infoExclusao_cpfTrab text,
        infoExclusao_perApur text,
        recibo_nrRecibo text
    )
    """)


def add(dados:dict):
    """ adiciona uma nova tarefa """
    
    colunas = ', '.join(dados.keys()) #lista de colunas separadas por virgula
    curingas = ', '.join('?' * len(dados)) #quantidade de parametros ? separados por virgulas
    
    sql = 'INSERT INTO s3000 ({}) VALUES ({})'.format(colunas, curingas)
    valores = [int(x) if isinstance(x, bool) else x for x in dados.values()]
    

    conn.execute(sql, valores)
    conn.commit()

def limpar_registros():
    """ exclui todos os registros da tabala s5001 """
    conn.execute("delete from s3000")
    conn.commit()