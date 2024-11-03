# Análise de Elegibilidade para Empréstimo Bancário com Redes Bayesianas

Este projeto foi desenvolvido como parte da disciplina de **Inteligência Artificial** no Instituto Federal de Santa Catarina (IFSC). O sistema utiliza **Redes Bayesianas** para analisar dados dos usuários e determinar a elegibilidade para a concessão de empréstimos bancários.

## Índice
- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Execução](#instalação-e-execução)
- [Endpoints](#endpoints)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Sobre o Projeto
O objetivo deste sistema é analisar automaticamente os dados do usuário e prever sua elegibilidade para um empréstimo, com base em probabilidades calculadas pela Rede Bayesiana. A Rede é construída a partir de parâmetros como renda, histórico de crédito, entre outros fatores relevantes.

## Funcionalidades
- Recebe e valida dados dos usuários via API.
- Processa os dados para gerar um modelo probabilístico.
- Retorna um status de elegibilidade para o empréstimo baseado na análise probabilística.

## Estrutura do Projeto
- **app/models**: Modelos Pydantic utilizados para validação de dados de entrada e saída.
- **app/routes**: Definição das rotas da API utilizando FastAPI.
- **app/calculate.py**: Funções de cálculo da Rede Bayesiana para determinar a probabilidade de aprovação de empréstimo.

### Pré-requisitos
- Python 3.11 ou superior
- FastAPI
- Uvicorn

### Passos para Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-projeto.git
    cd seu-projeto
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # Para Linux/macOS
    .\env\Scripts\activate   # Para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o servidor FastAPI com Uvicorn:
    ```bash
    uvicorn app.main:app --reload
    ```

5. Acesse a documentação da API:
   - Documentação Interativa (Swagger UI): `http://127.0.0.1:8000/docs`
   - Documentação Redoc: `http://127.0.0.1:8000/redoc`

## Endpoints
### POST `/api/receive-data`
Recebe e valida os dados do usuário, aplicando as regras da Rede Bayesiana para calcular a elegibilidade de empréstimo.

Exemplo de payload de envio:
```json
{
  "age": 0,
  "sex": 0,
  "job": ,
  "housing": 0,
  "saving_accounts": 0,
  "checking_account": 0,
  "credit_amount": 100,
  "duration": 30,
  "purpose": 4
}
```

Exemplo de payload de recebimento:
```json
{
  "emprestimo_valido": true
}
