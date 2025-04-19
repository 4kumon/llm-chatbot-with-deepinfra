
# Descrição

Este projeto cria um chatbot local em linha de comando utilizando o modelo gemma3:1b via Ollama. Ele serve como uma base sólida para a criação de interfaces conversacionais privadas, rápidas e que não dependem da internet ou de APIs de terceiros.

O modelo gemma3:1b é um exemplo de *Small Language Model* (SLM), ou "Modelo de Linguagem Pequeno". Modelos como o gemma3:1b são versões compactas de modelos de linguagem maiores, com menos parâmetros e requerimentos computacionais, o que torna possível sua execução em dispositivos locais com recursos limitados.

Por ser modular, o chatbot pode ser expandido com:
- Autenticação de usuários
- Histórico de conversas
- Interface web com Flask ou Streamlit
- Integração com bancos de dados
- Suporte a múltiplos modelos

É ideal para quem deseja estudar o funcionamento de LLMs locais, criar protótipos de AI LLM rápidos, ou garantir mais controle e privacidade na execução de modelos de linguagem.

## Tecnologias

- 🧠 **Ollama** – para execução local do modelo de AI LLM gemma3:1b (um SLM poderoso). Ollama é um *backend* baseado no Llama CPP, um framework que permite a execução eficiente de modelos de linguagem em plataformas locais.
- 🧩 **Llama CPP** – Llama CPP é uma implementação otimizada em C++ do modelo Llama, que visa reduzir o uso de memória e melhorar o desempenho, permitindo a execução de LLMs em dispositivos com menos recursos. Ele é amplamente utilizado em sistemas de *backends* como o Ollama.
- 🐍 **Python 3.8+**
- 📦 **requests** – biblioteca Python para comunicação com o servidor local do Ollama

## O que é Quantização?

A quantização é um processo técnico usado para reduzir a precisão dos parâmetros de um modelo de linguagem sem perder sua capacidade de fazer previsões precisas. Em modelos de grande porte, como os LLMs, a quantização ajuda a diminuir o consumo de memória e o poder de processamento necessário para rodar esses modelos. A quantização permite que os modelos sejam mais leves e rápidos, tornando-os ideais para uso local em dispositivos com menos recursos, como no caso do modelo gemma3:1b.

## Requisitos para rodar o modelo

Para rodar o modelo gemma3:1b localmente com o Ollama, é necessário um sistema com os seguintes requisitos mínimos:
- **1 GB de RAM**
- **CPU Quad Core**

Esses requisitos são suficientes devido à otimização do modelo e ao uso da quantização.

## Estrutura

```
ollama-chatbot-cli/
├── chatbot.py
├── config.py
├── main.py
├── requirements.txt
└── .env
```

## Instalação

Clone este repositório e instale as dependências usadas no Python:

```bash
git clone https://github.com/4kumon/ollama-chatbot-cli.git
cd ollama-chatbot-cli
pip install -r requirements.txt
```

[Clique aqui para baixar](https://ollama.com/download) e instalar o Ollama para seu sistema operacional

Carregue o modelo ```gemma3:1b```:

```bash
ollama run gemma3:1b
```

Isso iniciará um servidor local em ```http://localhost:11434```.

## Uso

Com o Ollama rodando em segundo plano:

```bash
python main.py
```

Você poderá conversar com o modelo diretamente pelo terminal.

## Diagrama UML

```mermaid
sequenceDiagram
    participant U as Usuário
    participant CLI as Chatbot (Terminal)
    participant Ollama as Modelo Local (gemma3:1b)

    U->>CLI: Digita uma pergunta
    CLI->>Ollama: Envia prompt para geração
    Ollama-->>CLI: Retorna resposta
    CLI-->>U: Mostra resposta
```
