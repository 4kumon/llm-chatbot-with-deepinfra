import requests

class Chatbot:
    def __init__(self, model="gemma3:1b", endpoint="http://localhost:11434/api/generate"):
        self.model = model
        self.endpoint = endpoint

    def ask(self, prompt):
        response = requests.post(self.endpoint, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })
        return response.json().get("response", "Erro ao gerar resposta.")

    def run(self):
        print("Digite sua pergunta (ou 'sair' para encerrar):")
        while True:
            user_input = input("Você: ")
            if user_input.lower() == "sair":
                break
            reply = self.ask(user_input)
            print("Chatbot:", reply.strip())
