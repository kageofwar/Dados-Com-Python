import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv('bolsaFamiliaBR2004-2022.csv', sep=";")

table = table.iloc[:, :-1]
table_numeric = table.loc[:, ['Sigla'] + list(table.loc[:, '2012':"2019"])]
table_numeric.set_index('Sigla', inplace=True)

total_por_ano = table_numeric.sum(axis=0)

ax = total_por_ano.plot(kind='bar', color='blue')
plt.title("Valor total gasto em cada ano com Bolsa familia")
plt.xlabel("Ano")
plt.ylabel("Total de gastos em dezenas de milhões de reais")

plt.show()
