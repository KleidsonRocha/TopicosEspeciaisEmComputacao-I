# Análise da Frota de Veículos no Rio Grande do Sul

Este projeto realiza uma análise de mineração de dados sobre a frota de veículos no estado do Rio Grande do Sul, Brasil. Utilizando dados abertos do governo do estado, o objetivo é identificar padrões e agrupar municípios com base na composição de suas frotas veiculares.

## Conteúdo do Repositório

-   `data_prep_rs.py`: Script Python para pré-processamento e agregação do dataset original.
-   `data_mining_rs.py`: Script Python para aplicação do algoritmo de agrupamento K-Means e análise dos clusters.
-   `visualizations_rs.py`: Script Python para geração de gráficos e visualizações dos resultados do agrupamento.
-   `frota_veiculos_rs_agregado.csv`: Dataset pré-processado e agregado, contendo a frota de veículos por tipo e município.
-   `frota_veiculos_rs_com_clusters.csv`: Dataset com os municípios e seus respectivos clusters atribuídos.
-   `elbow_method_rs.png`: Gráfico do método do cotovelo, utilizado para determinar o número ótimo de clusters.
-   `vehicle_type_distribution_by_cluster_rs.png`: Gráfico de barras mostrando a média dos tipos de veículos por cluster.
-   `relatorio_frota_veiculos_rs.pdf`: Relatório técnico detalhado sobre o projeto, incluindo metodologia, resultados e conclusões.
-   `README.md`: Este arquivo, explicando o projeto e como reproduzir a análise.

## Como Reproduzir a Análise

Para reproduzir a análise, siga os passos abaixo:

### 1. Pré-requisitos

Certifique-se de ter o Python 3.x instalado em seu sistema. As bibliotecas necessárias podem ser instaladas via `pip`:

```bash
pip install pandas scikit-learn matplotlib seaborn
```

### 2. Obtenção dos Dados

O dataset original (`VEI_DADOS_ABERTOS_20190513_1.CSV`) pode ser baixado do portal de Dados Abertos do Governo do Estado do Rio Grande do Sul:

[https://dados.rs.gov.br/dataset/frota-veiculos-em-circulacao](https://dados.rs.gov.br/dataset/frota-veiculos-em-circulacao)

Faça o download do arquivo `.zip` e descompacte-o na pasta `downloads` dentro do diretório do projeto. O nome do arquivo CSV deve ser `VEI_DADOS_ABERTOS_20190513_1.CSV`.

### 3. Execução dos Scripts

Execute os scripts Python na seguinte ordem:

1.  **Pré-processamento dos Dados:**

    ```bash
    python data_prep_rs.py
    ```
    Este script irá ler o dataset original, realizar a agregação por município e tipo de veículo, e salvar o resultado em `frota_veiculos_rs_agregado.csv`.

2.  **Aplicação do K-Means:**

    ```bash
    python data_mining_rs.py
    ```
    Este script aplicará o algoritmo K-Means ao dataset agregado, gerará o gráfico do método do cotovelo (`elbow_method_rs.png`) e salvará o dataset com os clusters atribuídos em `frota_veiculos_rs_com_clusters.csv`.

3.  **Geração de Visualizações:**

    ```bash
    python visualizations_rs.py
    ```
    Este script criará o gráfico de distribuição dos tipos de veículos por cluster (`vehicle_type_distribution_by_cluster_rs.png`) e exibirá os top 5 municípios para cada cluster no console.

### 4. Geração do Relatório

O relatório técnico em PDF (`relatorio_frota_veiculos_rs.pdf`) é gerado a partir do arquivo Markdown `report_rs.md` utilizando a ferramenta `manus-md-to-pdf` (disponível no ambiente de execução deste projeto). Se você estiver reproduzindo localmente, pode usar ferramentas como `pandoc` para converter o Markdown para PDF:

```bash
pandoc report_rs.md -o relatorio_frota_veiculos_rs.pdf
```

## Análise e Resultados

Os resultados da análise de agrupamento revelam perfis distintos de municípios no Rio Grande do Sul com base na composição de suas frotas veiculares. Foram identificados quatro clusters principais, que variam desde municípios de pequeno porte com frotas modestas até as grandes metrópoles com frotas massivas e diversificadas. Detalhes completos sobre a interpretação dos clusters e as visualizações geradas podem ser encontrados no `relatorio_frota_veiculos_rs.pdf`.



