"""
Script para interagir com o MongoDB usando pymongo.

Conecta-se a um banco de dados MongoDB e realiza as seguintes operações:
1. Adiciona o campo 'id_cliente' à lista de clientes.
2. Exclui as coleções existentes, se existirem.
3. Cria coleções para clientes e contas.
4. Insere dados das listas de clientes e contas nas respectivas coleções.
5. Imprime as listas de clientes e contas.

"""

import pprint
import pymongo as pym


client = pym.MongoClient(
    #<ENDEREÇO_MONGO_DB>
)

db = client.test
# colletion = db.test_colletion

# Adiciona o campo id_cliente à lista de clientes
clientes = [
    {
        "id_cliente": 1,
        "nome": "Ana Silva",
        "cpf": "000.000.000-00",
        "endereco": "Rua das Flores, 123",
    },
    {
        "id_cliente": 2,
        "nome": "João Souza",
        "cpf": "111.111.111-11",
        "endereco": "Avenida Brasil, 456",
    },
    {
        "id_cliente": 3,
        "nome": "Maria Oliveira",
        "cpf": "222.222.222-22",
        "endereco": "Rua da Paz, 789",
    },
    {
        "id_cliente": 4,
        "nome": "Pedro Santos",
        "cpf": "333.333.333-33",
        "endereco": "Rua da Alegria, 1011",
    },
    {
        "id_cliente": 5,
        "nome": "Camila Costa",
        "cpf": "444.444.444-44",
        "endereco": "Rua da Esperança, 1213",
    },
    {
        "id_cliente": 6,
        "nome": "Bruno Ferreira",
        "cpf": "555.555.555-55",
        "endereco": "Rua da Felicidade, 1415",
    },
    {
        "id_cliente": 7,
        "nome": "Luana Rodrigues",
        "cpf": "666.666.666-66",
        "endereco": "Rua do Amor, 1617",
    },
    {
        "id_cliente": 8,
        "nome": "Eduardo Martins",
        "cpf": "777.777.777-77",
        "endereco": "Rua da Amizade, 1819",
    },
    {
        "id_cliente": 9,
        "nome": "Gabriela Pereira",
        "cpf": "888.888.888-88",
        "endereco": "Rua da Família, 2021",
    },
    {
        "id_cliente": 10,
        "nome": "Rafael Azevedo",
        "cpf": "999.999.999-99",
        "endereco": "Rua da Prosperidade, 2223",
    },
]

contas = [
    {
        "tipo": "Conta corrente",
        "agencia": "0001",
        "num": 1,
        "id_cliente": 1,
        "saldo": 5700.0,
    },
    {
        "tipo": "Conta corrente",
        "agencia": "0001",
        "num": 2,
        "id_cliente": 2,
        "saldo": 23500.0,
    },
    {
        "tipo": "Poupança",
        "agencia": "0001",
        "num": 3,
        "id_cliente": 3,
        "saldo": 12500.0,
    },
    {
        "tipo": "Conta corrente",
        "agencia": "0001",
        "num": 4,
        "id_cliente": 4,
        "saldo": 500.0,
    },
    {
        "tipo": "Investidor",
        "agencia": "0001",
        "num": 5,
        "id_cliente": 5,
        "saldo": 57600.0,
    },
    {
        "tipo": "Conta corrente",
        "agencia": "0001",
        "num": 6,
        "id_cliente": 6,
        "saldo": 5300.0,
    },
    {
        "tipo": "Conta corrente",
        "agencia": "0001",
        "num": 7,
        "id_cliente": 7,
        "saldo": 512300.0,
    },
    {
        "tipo": "Investidor",
        "agencia": "0001",
        "num": 8,
        "id_cliente": 8,
        "saldo": 123500.0,
    },
    {
        "tipo": "Conta corrente",
        "agencia": "0001",
        "num": 9,
        "id_cliente": 9,
        "saldo": 50340.0,
    },
    {
        "tipo": "Poupança",
        "agencia": "0001",
        "num": 10,
        "id_cliente": 10,
        "saldo": 4500.0,
    },
]


# Nome da coleção
CLIENTES_COLLECTION_NAME = "clientes"
CONTAS_COLLECTION_NAME = "contas"


db.drop_collection(CLIENTES_COLLECTION_NAME)
db.drop_collection(CONTAS_COLLECTION_NAME)


clientes_collection = db[CLIENTES_COLLECTION_NAME]
contas_collection = db[CONTAS_COLLECTION_NAME]


cliente_collection = db.clientes
cliente_collection.insert_many(clientes)


conta_collection = db.contas
conta_collection.insert_many(contas)

pprint.pprint(clientes)
pprint.pprint(contas)
