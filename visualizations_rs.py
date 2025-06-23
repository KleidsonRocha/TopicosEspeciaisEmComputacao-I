import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o DataFrame com os clusters
df_clustered_rs = pd.read_csv("frota_veiculos_rs_com_clusters.csv")

# Selecionar as colunas numéricas para análise (tipos de veículos)
vehicle_type_cols_rs = [col for col in df_clustered_rs.columns if col not in ["MUNICIPIO", "TOTAL", "Cluster"]]

# Análise da distribuição dos tipos de veículos por cluster
# Criar um DataFrame com as médias dos tipos de veículos por cluster
cluster_means_rs = df_clustered_rs.groupby("Cluster")[vehicle_type_cols_rs].mean()

# Plotar a distribuição dos tipos de veículos para cada cluster
# Usar um gráfico de barras para comparar as médias
plt.figure(figsize=(15, 8))
cluster_means_rs.T.plot(kind='bar', figsize=(15, 8), colormap='viridis')
plt.title('Média dos Tipos de Veículos por Cluster (Frota RS)')
plt.xlabel('Tipo de Veículo')
plt.ylabel('Média da Frota')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('vehicle_type_distribution_by_cluster_rs.png')
plt.close()

print('Gráfico de distribuição dos tipos de veículos por cluster salvo como vehicle_type_distribution_by_cluster_rs.png')

# Visualizar a distribuição geográfica dos clusters (listando alguns municípios por cluster)
for cluster_id in sorted(df_clustered_rs["Cluster"].unique()):
    print(f"\nTop 5 Municípios no Cluster {cluster_id}:")
    print(df_clustered_rs[df_clustered_rs["Cluster"] == cluster_id]["MUNICIPIO"].head().to_markdown(index=False))


