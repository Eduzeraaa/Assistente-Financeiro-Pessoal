# Assistente Financeiro Pessoal com IA

Um agent financeiro inteligente desenvolvido com Python, LangChain, MCP e MongoDB.

O sistema interpreta mensagens do usuário, registra movimentações financeiras, consulta saldo atualizado e simula compras futuras com persistência real em banco de dados.

---

## Funcionalidades

- Registrar entradas e saídas de dinheiro
- Consultar saldo atual
- Simular compras futuras
- Persistência de dados com MongoDB
- Uso inteligente de tools via MCP

---

## Tecnologias

- Python
- LangChain
- LangGraph
- MCP (Model Context Protocol)
- FastMCP
- MongoDB
- Groq API
- Llama 3.3 70B
- PyMongo

---

## Como Funciona

Fluxo principal:

```text
Usuário
↓
LLM
↓
Agent
↓
MCP Client
↓
MCP Server
↓
Tools
↓
MongoDB
↓
Resposta final
```
A LLM interpreta a intenção da mensagem e escolhe automaticamente a tool mais adequada.

## Exemplos

### Registrar movimentação

Recebi 150 reais.

### Consultar saldo

Qual meu saldo atual?

### Simular compra

Se eu gastar 300 reais com um monitor?

## Por que MCP?

O MCP desacopla as tools da LLM, deixando a arquitetura mais organizada, escalável e profissional.
MCP não deixa o agent mais inteligente — deixa o sistema mais inteligente.
