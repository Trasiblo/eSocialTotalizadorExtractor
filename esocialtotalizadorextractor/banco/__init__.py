import sqlite3
from esocialtotalizadorextractor.banco.relatorio import relatorio as rel
from esocialtotalizadorextractor.banco.relatorio5002 import relatorio5002 as rel5002


"""banco de dados
"""
conn = sqlite3.connect("xmls.db")


relatorio = rel(conn)
relatorio5002 = rel5002(conn)
