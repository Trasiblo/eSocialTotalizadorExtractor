import esocialtotalizadorextractor.banco.db as db
import locale

def formatDinheiro(vlr):
    #locale.setlocale(locale.LC_ALL, 'pt')
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    valor = locale.currency(vlr, grouping=False, symbol=None)
    return valor

comunicacao = db.conn
#db.criar_tabela_todo()
#db.add_tarefa('teste')

#db.criar_tabela_s3000(comunicacao)
#db.criar_tabela_s5001(comunicacao)

valores = db.get_valor(comunicacao)

valor = valores.fetchall()

colunas = valores.description

#pegar nome das colunas
#for r1 in colunas:
    #print(r1[0])

#converter dados

for r in valor:
    rg = []
    for c in r:
        
        if (type(c) == float):
            c = formatDinheiro(c)
        rg.append(c)
    print(rg)
        

#print(valor[0][0])
