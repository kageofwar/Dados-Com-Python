import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
table = pd.read_csv('bolsaFamiliaBR2004-2022.csv', sep=";")

# Removendo a última coluna, pois ela está vazia
table = table.iloc[:, :-1]

# Selecionando apenas as colunas numéricas a partir de 2012, incluindo a coluna "Sigla"
table_numeric = table.loc[:, ['Sigla'] + list(table.loc[:, '2012':"2019"])]

# Configurando a coluna "Sigla" como índice
table_numeric.set_index('Sigla', inplace=True)

# Somando os valores ao longo das colunas (estados) para cada ano
total_por_ano = table_numeric.sum(axis=0)

ax = total_por_ano.plot(kind='bar', color='blue')
plt.title("Valor total gasto em cada ano com Bolsa familia")
plt.xlabel("Ano")
plt.ylabel("Total de gastos em dezenas de milhões de reais")

plt.show()
