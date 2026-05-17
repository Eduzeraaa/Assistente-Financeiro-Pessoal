import os
from datetime import date
from dotenv import load_dotenv
from pymongo import MongoClient
from fastmcp import FastMCP

load_dotenv()

mcp = FastMCP('Financeiro')

client = MongoClient(os.getenv('MONGODB_URI'))

db = client.financas

def buscar_saldo():
    saldo_atual = db.movimentacoes.find_one(
        {'User_id': 'edu123'},
        sort=[("_id", -1)]
    )

    if saldo_atual is None:
        return float(0)


    return float(saldo_atual["Saldo Total"])


@mcp.tool
def registrar_movimentacao(nova_movimentacao_bancaria: float):
    """Atualiza o saldo do usuário com base em uma nova movimentação bancária.
    Lembre-se que o usuário pode ter gastado o dinheiro em algo, ou recebido dinheiro de alguém, logo, o saldo pode aumentar ou diminuir.
    Interprete bem a mensagem do usuário para entender se há uma movimentação, e se é um gasto ou um ganho.
    Apenas execute essa tool se o usuário mencionar uma movimentação bancária, caso contrário, não a execute e responda normalmente."""

    dados = {
        'User_id': 'edu123',
        'Movimentação': nova_movimentacao_bancaria,
        'Saldo Total': (buscar_saldo() + nova_movimentacao_bancaria),
        'Data': date.today().strftime("%d/%m/%Y")
    }

    db.movimentacoes.insert_one(dados)

    return nova_movimentacao_bancaria

@mcp.tool
def consultar_saldo():
    """Consulta o saldo atual do usuário. Apenas execute essa tool se o usuário perguntar sobre o saldo atual, caso contrário, responda normalmente."""
    return buscar_saldo()


@mcp.tool
def simular_compra(gasto_simulado: float) -> float:
    """Simula uma compra, e como ela pode impactar nas finanças do usuário. A ideia aqui é que o usuário possa ter uma noção de como um gasto pode 
    impactar no saldo atual, e se ele tem dinheiro suficiente para realizar a compra. 
    Apenas execute essa tool se o usuário mencionar algo sobre simular um gasto ou uma compra, caso contrário, responda normalmente."""
    print(f'Com o seu saldo atual de R${buscar_saldo()}, simulando um gasto de R${gasto_simulado}, você ficaria num saldo de R${buscar_saldo() - gasto_simulado}.')
    
    return buscar_saldo() - gasto_simulado


if __name__ == "__main__":
    try:
        mcp.run()
    except Exception as e:
        print(f'Houve um erro: {e}')
