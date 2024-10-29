# Relatório de Vendas API

Este projeto é uma API construída com Flask e Pandas, que permite o upload de um arquivo CSV contendo dados de vendas e gera relatórios detalhados sobre os clientes, empresas e produtos. Além disso, uma tabela visual das vendas é gerada utilizando a biblioteca Matplotlib.

## Funcionalidades

- **Upload de CSV**: Permite o upload de um arquivo CSV com informações de vendas.
- **Relatório de Vendas**: Gera um relatório por cliente e produtos comprados.
- **Visualização de Tabelas**: Exibe os dados de vendas em formato de tabela utilizando Matplotlib.
- **Testes Automatizados**: Testes foram configurados com pytest para garantir a integridade das rotas.

## Estrutura do Projeto

```bash
project/
│
├── app/
│   ├── __init__.py            # Inicialização da aplicação Flask
│   ├── routes.py              # Definição das rotas
│   ├── services.py            # Lógica de manipulação do CSV e geração de relatório
│   ├── utils.py               # Funções utilitárias (geração de tabela)
│
├── data/
│   └── exemplo.csv            # Arquivo CSV de exemplo
│
├── tests/
│   └── test_routes.py         # Testes para as rotas Flask
│
├── README.md                  # Documentação do projeto
├── requirements.txt           # Arquivo com as dependências
└── app.py                     # Arquivo principal para rodar a aplicação
```

## Tecnologias Utilizadas

- Flask: Framework web para construção da API.
- Pandas: Biblioteca para manipulação de dados.
- Matplotlib: Biblioteca para exibição de tabelas gráficas.

## Pré-requisitos
- Python 3.7 ou superior
- Pip para gerenciar pacotes

## Instalação 
1. Clone o repositório:
```bash
git clone https://github.com/vinicius-augusto1/api-python-project
```
2. Navegue até o diretório do projeto:
```bash
cd project
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

1. Inicie a aplicação:
```bash
python app.py
    ou 
python3 app.py
```

A aplicação estará disponível em: http://localhost:5000/.

2. Envie uma requisição POST para a rota /relatorio-vendas com o arquivo CSV contendo os seguintes campos:
```bash
cliente,empresa,produto,valor,quantidade
João,Loja A,Produto 1,100,2
Maria,Loja B,Produto 2,50,3
```

3. Via Postman 
- Inicie a API localmente com python api_vendas.py.
- Abra o Postman.
- Faça uma requisição POST para a URL: http://127.0.0.1:5000/relatorio-vendas.
- No Body, selecione form-data, com a chave file do tipo File e adicione o arquivo CSV.
- Envie a requisição. A API retornará o relatório no formato JSON e exibirá a tabela com o resumo.

4. A resposta será um relatório, incluindo uma tabela visual em imagem das vendas.
