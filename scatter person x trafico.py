import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados de tráfico
trafico_data = pd.read_csv('trafico-absolut.csv', delimiter=';')
trafico_data = trafico_data.set_index('UF')

# Carregar os dados do Bolsa Família por pessoas
bolsa_familia_data = pd.read_csv('BolsaFamiliaPessoas.csv', delimiter=';')
bolsa_familia_data = bolsa_familia_data.set_index('Sigla')

# Encontrar a interseção dos anos disponíveis para ambas as séries temporais
anos_intersecao = trafico_data.columns.intersection(bolsa_familia_data.columns)

# Filtrar os dados para incluir apenas os anos disponíveis em ambas as séries temporais
trafico_data = trafico_data[anos_intersecao]
bolsa_familia_data = bolsa_familia_data[anos_intersecao]

# Normalizar os dados para calcular a correlação de Pearson
trafico_norm = (trafico_data - trafico_data.mean()) / trafico_data.std()
bolsa_familia_norm = (bolsa_familia_data - bolsa_familia_data.mean()) / bolsa_familia_data.std()

# Calcular a correlação de Pearson
correlacao_pearson = trafico_norm.T.corrwith(bolsa_familia_norm.T)

# Criar um gráfico de dispersão para cada estado
plt.figure(figsize=(12, 8))

for uf in trafico_data.index:
    x = trafico_norm.loc[uf].values
    y = bolsa_familia_norm.loc[uf].values

    # Calcular e mostrar o coeficiente de correlação de Pearson para cada estado
    sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson[uf]:.2f}', s=100, alpha=0.7)

# Adicionar rótulos aos eixos e título ao gráfico
plt.xlabel('Número de Ocorrências de Tráfico (Normalizado)')
plt.ylabel('Beneficiários do Bolsa Família por Pessoas (Normalizado)')
plt.title('Relação entre Tráfico e Bolsa Família por Pessoas (por Estado)')

plt.legend()
plt.grid(True)
plt.show()
