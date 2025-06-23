import pandas as pd

# Definir o caminho do arquivo
file_path = "/home/ubuntu/downloads/VEI_DADOS_ABERTOS_20190513_1.CSV"
output_file_path = "frota_veiculos_rs_agregado.csv"

# Definir as colunas relevantes para a agregação
# "especie" parece ser o tipo de veículo e " munic_emplamento" o município
relevant_columns = ["especie", " munic_emplamento"]

# Inicializar um dicionário para armazenar as contagens agregadas
aggregated_data = {}

chunksize = 100000  # Processar 100.000 linhas por vez

print(f"Iniciando leitura do arquivo em chunks de {chunksize} linhas para agregação...")

# Iterar sobre o arquivo em chunks
for i, chunk in enumerate(pd.read_csv(file_path, encoding="latin1", sep=";", decimal=",", chunksize=chunksize, on_bad_lines="skip")):
    print(f"Processando chunk {i+1}...")
    
    # Filtrar apenas as colunas relevantes
    chunk_filtered = chunk[relevant_columns]
    
    # Remover linhas com valores NaN nas colunas relevantes
    chunk_filtered = chunk_filtered.dropna(subset=relevant_columns)
    
    # Agrupar por espécie e município e contar
    counts = chunk_filtered.groupby([" munic_emplamento", "especie"]).size().reset_index(name="count")
    
    # Atualizar o dicionário agregado
    for _, row in counts.iterrows():
        municipio = row[" munic_emplamento"]
        especie = row["especie"]
        count = row["count"]
        
        if municipio not in aggregated_data:
            aggregated_data[municipio] = {"TOTAL": 0}
        if especie not in aggregated_data[municipio]:
            aggregated_data[municipio][especie] = 0
            
        aggregated_data[municipio][especie] += count
        aggregated_data[municipio]["TOTAL"] += count

print("Agregação de dados concluída. Convertendo para DataFrame...")

# Converter o dicionário agregado para DataFrame
df_aggregated = pd.DataFrame.from_dict(aggregated_data, orient="index")
df_aggregated.index.name = "MUNICIPIO"
df_aggregated = df_aggregated.reset_index()

# Preencher valores NaN (tipos de veículos que não existem em alguns municípios) com 0
df_aggregated = df_aggregated.fillna(0)

# Reordenar colunas para ter MUNICIPIO e TOTAL no início
cols = ["MUNICIPIO", "TOTAL"] + [col for col in df_aggregated.columns if col not in ["MUNICIPIO", "TOTAL"]]
df_aggregated = df_aggregated[cols]

# Salvar o DataFrame agregado em um novo arquivo CSV
df_aggregated.to_csv(output_file_path, index=False)

print(f"Dataset agregado salvo como {output_file_path}")
print(df_aggregated.head().to_markdown(index=False))
print(df_aggregated.info())

