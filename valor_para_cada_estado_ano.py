import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv('bolsaFamiliaBR2004-2022.csv', sep=";")

table_numeric = table.loc[:, ['Sigla'] + list(table.loc[:, '2012':'2019'])]
table_numeric.set_index('Sigla', inplace=True)
table_numeric_T = table_numeric.T

for estado in table_numeric_T.columns:
    plt.plot(table_numeric_T.index, table_numeric_T[estado], label=estado)

plt.title("Total de valor gasto com Bolsa Familia em cada estado para cada ano")
plt.grid(False)
plt.box(True)
plt.legend(title="Estado")
plt.xlabel("Ano")
plt.ylabel("Gastos em milhões")
plt.show()
