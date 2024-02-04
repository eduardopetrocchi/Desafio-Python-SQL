# Desafio Python SQL

Este projeto consiste em um script Python interagindo com o MongoDB usando pymongo e outro script utilizando SQLAlchemy para interação com um banco de dados PostgreSQL. O objetivo principal é demonstrar a manipulação de dados em dois tipos diferentes de bancos de dados.

## Funcionalidades

### MongoDB (Pymongo)

1. Adiciona o campo 'id_cliente' à lista de clientes.
2. Exclui coleções existentes, se existirem.
3. Cria coleções para clientes e contas.
4. Insere dados das listas de clientes e contas nas respectivas coleções.
5. Imprime as listas de clientes e contas.

### PostgreSQL (SQLAlchemy)

1. Define duas classes, `Cliente` e `Conta`, representando clientes e contas em uma loja online.
2. Estabelece um relacionamento entre `Cliente` e `Conta`.
3. Cria tabelas no banco de dados PostgreSQL.
4. Adiciona dados de clientes e contas.
5. Executa consultas SQL como exemplos, incluindo seleção de clientes pares, impares, clientes com letra 'a' no nome, e lista ordenada por saldo decrescente.
6. Calcula o total de clientes cadastrados.

## Requisitos

- Certifique-se de ter um servidor MongoDB em execução para a parte do Pymongo.
- Para a parte do SQLAlchemy, é necessário um servidor PostgreSQL com as credenciais corretas.

## Como Executar

1. **MongoDB (Pymongo):**
   - Certifique-se de ter o MongoDB instalado e em execução.
   - Configure o endereço do MongoDB no script.
   - Execute o script Python.

2. **PostgreSQL (SQLAlchemy):**
   - Certifique-se de ter o PostgreSQL instalado e em execução.
   - Configure o endereço do PostgreSQL no script.
   - Execute o script Python.

Lembre-se de fornecer as credenciais adequadas ao se conectar ao PostgreSQL.

**Observação:** Estes scripts são destinados a fins educacionais e podem exigir ajustes dependendo do ambiente em que são executados.


## Autores

- [@eduardopetrocchi](https://www.github.com/eduardopetrocchi)

