import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados de homicídios
homicidios_data = pd.read_csv('homicidio2013-2019.csv', delimiter=';')
homicidios_data = homicidios_data.set_index('uf')

# Carregar os dados do Bolsa Família por pessoas
bolsa_familia_data = pd.read_csv('BolsaFamiliaPessoas.csv', delimiter=';')
bolsa_familia_data = bolsa_familia_data.set_index('Sigla')

# Encontrar a interseção dos anos disponíveis para ambas as séries temporais
anos_intersecao = homicidios_data.columns.intersection(bolsa_familia_data.columns)

# Filtrar os dados para incluir apenas os anos disponíveis em ambas as séries temporais
homicidios_data = homicidios_data[anos_intersecao]
bolsa_familia_data = bolsa_familia_data[anos_intersecao]

# Criar um gráfico de dispersão para cada estado
plt.figure(figsize=(12, 8))

for uf in homicidios_data.index:
    x = homicidios_data.loc[uf].values
    y = bolsa_familia_data.loc[uf].values

    # Calcular e mostrar o coeficiente de correlação de Pearson para cada estado
    correlacao_pearson = pd.Series(x).corr(pd.Series(y))
    sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')

# Adicionar rótulos aos eixos e título ao gráfico
plt.xlabel('Número de Homicídios')
plt.ylabel('Beneficiários do Bolsa Família por Pessoas')
plt.title('Relação entre Homicídios e Bolsa Família por Pessoas (por Estado)')

plt.legend()
plt.grid(True)
plt.show()
