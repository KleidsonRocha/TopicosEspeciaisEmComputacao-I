import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o DataFrame agregado
df_aggregated = pd.read_csv("frota_veiculos_rs_agregado.csv")

# Selecionar as colunas numéricas para o agrupamento (tipos de veículos)
# Excluir 'MUNICIPIO' e 'TOTAL' para o agrupamento
vehicle_type_cols = [col for col in df_aggregated.columns if col not in ["MUNICIPIO", "TOTAL"]]
X = df_aggregated[vehicle_type_cols]

# Normalizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determinar o número ideal de clusters usando o método do cotovelo (Elbow Method)
inertia = []
K_range = range(1, 11) # Testar de 1 a 10 clusters
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plotar o método do cotovelo
plt.figure(figsize=(10, 6))
plt.plot(K_range, inertia, marker='o')
plt.title('Método do Cotovelo para K-Means (Frota RS)')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Inércia')
plt.xticks(K_range)
plt.grid(True)
plt.savefig('elbow_method_rs.png')
plt.close()

print('Gráfico do método do cotovelo salvo como elbow_method_rs.png')

# Com base no gráfico do cotovelo (será analisado após a execução), vamos escolher um K.
# Para fins de demonstração, vamos começar com K=4 novamente.
k_optimal = 4

# Aplicar K-Means com o número ideal de clusters
kmeans = KMeans(n_clusters=k_optimal, random_state=42, n_init=10)
df_aggregated["Cluster"] = kmeans.fit_predict(X_scaled)

# Salvar o DataFrame com os clusters
df_aggregated.to_csv("frota_veiculos_rs_com_clusters.csv", index=False)

print(f'Agrupamento K-Means aplicado com {k_optimal} clusters para a frota do RS.')
print('DataFrame com clusters salvo como frota_veiculos_rs_com_clusters.csv')
print('Contagem de municípios por cluster:')
print(df_aggregated["Cluster"].value_counts().to_markdown())

# Analisar as características de cada cluster (média dos tipos de veículos por cluster)
cluster_centers = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=vehicle_type_cols)
cluster_centers["Cluster"] = range(k_optimal)
cluster_centers = cluster_centers.set_index("Cluster")
print('\nCaracterísticas médias dos clusters:')
print(cluster_centers.to_markdown())

