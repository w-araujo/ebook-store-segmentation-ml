## Estrutura do Projeto

```plaintext
project-root/
│
├── data/
│   ├── ebook_store.csv               # Arquivo de dados em Excel
│   └── ebook_store_validation.csv    # Dados de validação (gerados após o pré-processamento)
│
├── src/
│   ├── pre_process.py          # Script para pré-processar os dados
│   ├── train_model.py          # Script para treinar o modelo K-means
│   ├── validate_model.py       # Script para validar o modelo usando silhouette score
│
├── models/
│   ├── modelo_atual.pkl        # Última versão do modelo em produção
│   └── modelo_novo.pkl         # Novo modelo treinado
│
├── .github/
│   └── workflows/
│       └── mlops_pipeline.yml  # Arquivo do GitHub Actions para CI/CD
│
├── requirements.txt            # Bibliotecas necessárias para o projeto
└── README.md                   # Documentação do projeto
```
