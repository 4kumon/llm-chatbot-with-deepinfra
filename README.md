
### Estrutura
```
llm-chatbot-with-deepinfra/
├── chatbot.py
├── config.py
├── main.py
├── requirements.txt
└── .env
```

### Instalação
```bash
git clone https://github.com/seu-repo/llm-chatbot-with-deepinfra.git
cd llm-chatbot-with-deepinfra
pip install -r requirements.txt
```

### Configuração
Crie um arquivo .env para armazenar sua chave de API da DeepInfra:
```
DEEPINFRA_API_KEY=your-deepinfra-api-key
```


### Uso
```bash
python main.py
```

### Diagrama UML
```mermaid
sequenceDiagram
    participant U as Usuário
    participant F as ChatbotFrontend
    participant API as DeepInfra API
    U->>F: Faz pergunta
    F->>API: Envia pergunta
    API-->>F: Retorna resposta
    F-->>U: Exibe resposta
```
