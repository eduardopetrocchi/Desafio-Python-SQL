"""
Módulo que define as classes Cliente e Conta para representar clientes e
suas contas em uma loja online.

Classes:
    Cliente: Representa um cliente com informações como nome, CPF e endereço.
    Conta: Representa uma conta associada a um cliente,
            com informações como tipo, agência, número e saldo.

Relacionamentos:
    Cliente possui uma relação de um para muitos com Conta.

Uso:
    Para utilizar este módulo, crie instâncias das classes Cliente e Conta, 
    e estabeleça os relacionamentos entre elas.

"""

from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    create_engine,
    func,
    select,
)
from sqlalchemy.orm import Session, declarative_base, relationship

Base = declarative_base()


class Cliente(Base):
    """
    Classe que representa um cliente em uma loja online.

    Attributes:
        id_cliente (int): Identificador único do cliente.
        nome (str): Nome do cliente.
        cpf (str): Número do CPF do cliente.
        endereco (str): Endereço do cliente.

    Relationships:
        conta (relationship): Relacionamento com a tabela Conta.

    Methods:
        __init__(nome, cpf, endereco): Inicializa uma nova instância de Cliente.
        __repr__(): Retorna uma representação em string do objeto Cliente.

    """

    __tablename__ = "dados_cliente"

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(200))
    cpf = Column(String(15))
    endereco = Column(String(50))

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __init__(self, nome, cpf, endereco):
        """
        Inicializa uma nova instância de Cliente.

        Args:
            nome (str): Nome do cliente.
            cpf (str): Número do CPF do cliente.
            endereco (str): Endereço do cliente.

        Returns:
            None

        """
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def __repr__(self) -> str:
        """
        Retorna uma representação em string do objeto Cliente.

        Returns:
            str: Representação em string do objeto Cliente.

        """
        return f"Cliente(id_cliente={self.id_cliente}, nome={self.nome})"


class Conta(Base):
    """
    Classe que representa uma conta associada a um cliente.

    Attributes:
        id_conta (int): Identificador único da conta.
        tipo (str): Tipo da conta (e.g., "Conta corrente", "Poupança").
        agencia (str): Número da agência da conta.
        num (int): Número da conta.
        id_cliente (int): Identificador do cliente associado à conta.
        saldo (float): Saldo atual da conta.

    Relationships:
        cliente (relationship): Relacionamento com a tabela Cliente.

    Methods:
        __init__(tipo, agencia, id_cliente, saldo): Inicializa uma nova instância de Conta.
        __repr__(): Retorna uma representação em string do objeto Conta.

    """

    __tablename__ = "dados_conta"

    id_conta = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(String, default="0001")
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("dados_cliente.id_cliente"), nullable=True)
    saldo = Column(Float, default=0)

    cliente = relationship("Cliente", back_populates="conta")

    def __init__(self, tipo, agencia, id_cliente, saldo):
        """
        Inicializa uma nova instância de Conta.

        Args:
            tipo (str): Tipo da conta.
            agencia (str): Número da agência da conta.
            id_cliente (int): Identificador do cliente associado à conta.
            saldo (Float): Saldo inicial da conta.

        Returns:
            None

        """
        super().__init__()
        self.tipo = tipo
        self.agencia = agencia
        self.id_cliente = id_cliente
        self.num = id_cliente
        self.saldo = saldo

    def __repr__(self) -> str:
        """
        Retorna uma representação em string do objeto Conta.

        Returns:
            str: Representação em string do objeto Conta.

        """
        return (
            f"Conta(id_conta={self.id_conta}, "
            f"tipo={self.tipo}, "
            f"agencia={self.agencia}, "
            f"num={self.num}, "
            f"saldo={self.saldo})"
        )



engine = create_engine(
    "postgresql+psycopg2://postgres:<SENHA>@localhost/desafioInterligandoPythonSQL"
)


Base.metadata.drop_all(engine)  # type: ignore
Base.metadata.create_all(engine)  # type: ignore


with Session(engine) as session:
    clientes = [
        Cliente(nome="Ana Silva", cpf="000.000.000-00", endereco="Rua das Flores, 123"),
        Cliente(
            nome="João Souza", cpf="111.111.111-11", endereco="Avenida Brasil, 456"
        ),
        Cliente(
            nome="Maria Oliveira", cpf="222.222.222-22", endereco="Rua da Paz, 789"
        ),
        Cliente(
            nome="Pedro Santos", cpf="333.333.333-33", endereco="Rua da Alegria, 1011"
        ),
        Cliente(
            nome="Camila Costa", cpf="444.444.444-44", endereco="Rua da Esperança, 1213"
        ),
        Cliente(
            nome="Bruno Ferreira",
            cpf="555.555.555-55",
            endereco="Rua da Felicidade, 1415",
        ),
        Cliente(
            nome="Luana Rodrigues", cpf="666.666.666-66", endereco="Rua do Amor, 1617"
        ),
        Cliente(
            nome="Eduardo Martins",
            cpf="777.777.777-77",
            endereco="Rua da Amizade, 1819",
        ),
        Cliente(
            nome="Gabriela Pereira",
            cpf="888.888.888-88",
            endereco="Rua da Família, 2021",
        ),
        Cliente(
            nome="Rafael Azevedo",
            cpf="999.999.999-99",
            endereco="Rua da Prosperidade, 2223",
        ),
    ]
    session.add_all(clientes)

    contas = [
        Conta(tipo="Conta corrente", agencia="0001", id_cliente=1, saldo=5700),
        Conta(tipo="Conta corrente", agencia="0001", id_cliente=2, saldo=23500),
        Conta(tipo="Poupança", agencia="0001", id_cliente=3, saldo=12500),
        Conta(tipo="Conta corrente", agencia="0001", id_cliente=4, saldo=500),
        Conta(tipo="Investidor", agencia="0001", id_cliente=5, saldo=57600),
        Conta(tipo="Conta corrente", agencia="0001", id_cliente=6, saldo=5300),
        Conta(tipo="Conta corrente", agencia="0001", id_cliente=7, saldo=512300),
        Conta(tipo="Investidor", agencia="0001", id_cliente=8, saldo=123500),
        Conta(tipo="Conta corrente", agencia="0001", id_cliente=9, saldo=50340),
        Conta(tipo="Poupança", agencia="0001", id_cliente=10, saldo=4500),
    ]
    session.add_all(contas)

    session.commit()


print("Lista de clientes pares:")
stmt = select(Cliente).where(func.mod(Cliente.id_cliente, 2) == 0)
for cliente in session.scalars(stmt):
    print(cliente)

print("\nLista de clientes impares:")
stmt = select(Cliente).where(func.mod(Cliente.id_cliente, 2) != 0)
for cliente in session.scalars(stmt):
    print(cliente)

print("\nLista de cliente que contém letra 'a':")
stmt = select(Cliente).where(Cliente.nome.ilike("%a%"))
for cliente in session.scalars(stmt):
    print(cliente)


print("\nLista de cliente ordenado por saldo decrescente:")
stmt_join = (
    select(Cliente.nome, Conta.saldo, Conta.tipo)
    .join_from(Cliente, Conta)
    .order_by(Conta.saldo.desc())
)
for cliente, valor, tipo_conta in session.execute(stmt_join):
    print(f"O cliente {cliente} possui R$:{valor} na conta do tipo: {tipo_conta}")


print("\nTotal de clientes cadastrados: ")
stmt_count = select(func.count("*")).select_from(Cliente)
for total in session.scalars(stmt_count):
    print(total)
