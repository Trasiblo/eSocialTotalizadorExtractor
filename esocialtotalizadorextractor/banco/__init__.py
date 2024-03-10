import sqlite3
from banco.relatorio import relatorio as rel

"""banco de dados
"""
conn = sqlite3.connect("xmls.db")


relatorio = rel(conn)
