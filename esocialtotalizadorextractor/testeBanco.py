import esocialtotalizadorextractor.banco.db as db
import esocialtotalizadorextractor.banco as conexao
import locale
import pandas as pd

def formatDinheiro(vlr):
    #locale.setlocale(locale.LC_ALL, 'pt')
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    valor = locale.currency(vlr, grouping=False, symbol=None)
    return valor


#db.criar_tabela_todo()
#db.add_tarefa('teste')

#db.criar_tabela_s3000(comunicacao)
#db.criar_tabela_s5001(comunicacao)
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


valores = db.get_valor(conexao.conn)
valores.row_factory = dict_factory
valor = valores.fetchall()

df1 = pd.DataFrame(valor)

print(df1)
df1.to_csv('teste.csv',sep=';', index=False)

colunas = valores.description

#pegar nome das colunas
#for r1 in colunas:
    #print(r1[0])

#converter dados

#for r in valor:
#    rg = []
#   for c in r:
#       
#       if (type(c) == float):
#           c = formatDinheiro(c)
#       rg.append(c)
#   print(rg)



#print(valor[0][0])
