import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('BolsaFamiliaPessoas.csv', delimiter=';')

plt.bar(dados.columns[3:], dados.iloc[:, 3:].sum(), color='green')

plt.xlabel('Ano')
plt.ylabel('Número Total de Brasileiros Cadastrados')
plt.title('Bolsa Família - Número Total de Brasileiros Cadastrados por Ano (2012-2019)')
plt.show()
