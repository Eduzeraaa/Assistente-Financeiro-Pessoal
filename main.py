import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


load_dotenv()


async def construir_agente():
    caminho_mcp_financeiro = Path(__file__).parent / "mcp_financeiro.py"

    client_mcp = MultiServerMCPClient(
        {
            "Financeiro": {
                "command": "python",
                "args": [str(caminho_mcp_financeiro)],
                "transport": "stdio",
            }
        }
    )

    tools = await client_mcp.get_tools()

    model = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7,
        max_tokens=400,
    )

    agente_financeiro = create_agent(
        model=model,
        tools=tools,
        system_prompt="""
Você é um assistente financeiro pessoal.

Seja sempre objetivo, direto e claro.

Se o usuário mencionar recebimento ou gasto de dinheiro, utilize a ferramenta "registrar_movimentacao".

Se o usuário perguntar sobre saldo atual, utilize a ferramenta "consultar_saldo".

Se o usuário mencionar simular compra, gasto futuro ou impacto financeiro, utilize a ferramenta "simular_compra".

Responda normalmente para mensagens que não exigem tools.

Não use ferramentas desnecessariamente.

Use tools apenas quando realmente fizer sentido.
""",
    )

    return agente_financeiro


agente_financeiro = asyncio.run(construir_agente())


config = {
    "configurable": {
        "thread_id": "Gravação de teste do agente financeiro pessoal"
    }
}
