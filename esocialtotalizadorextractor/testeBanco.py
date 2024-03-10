import banco as conexao
import pandas as pd


rel = conexao.relatorio

valor = rel.get_valor()
df1 = pd.DataFrame(valor)

valor = rel.get_valor_analitico()
df2 = pd.DataFrame(valor)

arqExcel = pd.ExcelWriter('teste.xlsx')

df1.to_excel(arqExcel, index=False, float_format='%.2f', sheet_name='Resumo')
df2.to_excel(arqExcel, index=False, float_format='%.2f', sheet_name='Analitica')

arqExcel.close()