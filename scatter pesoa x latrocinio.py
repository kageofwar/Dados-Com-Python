import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados de latrocínio
latrocinio_data = pd.read_csv('latrocinio-absoluto.csv', delimiter=';')
latrocinio_data = latrocinio_data.set_index('UF')

# Carregar os dados do Bolsa Família por pessoas
bolsa_familia_data = pd.read_csv('BolsaFamiliaPessoas.csv', delimiter=';')
bolsa_familia_data = bolsa_familia_data.set_index('Sigla')

# Encontrar a interseção dos anos disponíveis para ambas as séries temporais
anos_intersecao = latrocinio_data.columns.intersection(bolsa_familia_data.columns)

# Filtrar os dados para incluir apenas os anos disponíveis em ambas as séries temporais
latrocinio_data = latrocinio_data[anos_intersecao]
bolsa_familia_data = bolsa_familia_data[anos_intersecao]

# Criar um gráfico de dispersão para cada estado
plt.figure(figsize=(12, 8))

for uf in latrocinio_data.index:
    x = latrocinio_data.loc[uf].values
    y = bolsa_familia_data.loc[uf].values

    # Calcular e mostrar o coeficiente de correlação de Pearson para cada estado
    correlacao_pearson = pd.Series(x).corr(pd.Series(y))
    sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')

# Adicionar rótulos aos eixos e título ao gráfico
plt.xlabel('Número de Latrocínios')
plt.ylabel('Beneficiários do Bolsa Família por Pessoas')
plt.title('Relação entre Latrocínios e Bolsa Família por Pessoas (por Estado)')

plt.legend()
plt.grid(True)
plt.show()
