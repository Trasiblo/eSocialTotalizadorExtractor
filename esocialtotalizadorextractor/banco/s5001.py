import sqlite3

from banco import conn

def criar_tabela():
    """ cria a tabela 'tarefa' caso ela não exista """
    conn.execute("""
    create table if not exists s5001 (
        --id text primary key,
        arquivo text,
        nrRecArqBase text,
        perApur text,
        cpfTrab text,
        tpCR text,
        vrCpSeg float,
        vrDescSeg float,
        nrInsc text,
        codLotacao text,
        matricula text,
        codCateg text,
        valor_baseInss float,
        valor_descInss float   
    )
    """)    


def add(dados:dict):
    """ adiciona uma nova tarefa """
    
    colunas = ', '.join(dados.keys()) #lista de colunas separadas por virgula
    curingas = ', '.join('?' * len(dados)) #quantidade de parametros ? separados por virgulas
    
    sql = 'INSERT INTO s5001 ({}) VALUES ({})'.format(colunas, curingas)
    valores = [int(x) if isinstance(x, bool) else x for x in dados.values()]
    
    conn.execute(sql, valores)
    conn.commit()

def limpar_registros():
    """ exclui todos os registros da tabala s5001 """
    conn.execute("delete from s5001")
    conn.commit()