## Estrutura do Projeto

```plaintext
project-root/
│
├── data/
│   ├── ebook_store.csv               # Arquivo de dados em Excel
│   └── ebook_store_preprocessed.csv  # Dados de validação (gerados após o pré-processamento)
│
├── src/
│   ├── pre_process.py                # Script para pré-processar os dados
│   ├── train_model.py                # Script para treinar o modelo K-means
│   ├── validate_model.py             # Script para validar o modelo usando silhouette score
│
├── models/
│   └── kmens_model.pkl               # Modelo treinado
|
├── production/
|   └── kmens_model.pkl               # Modelo em produção
|
├── .github/
│   └── workflows/
│       └── mlops_pipeline.yml        # Arquivo do GitHub Actions para CI/CD
│
├── requirements.txt                  # Bibliotecas necessárias para o projeto
└── README.md                         # Documentação do projeto
```
