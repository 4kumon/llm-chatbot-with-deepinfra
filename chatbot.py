import requests
import sys

class Chatbot:
    def __init__(self, model="gemma3:1b", endpoint="http://localhost:11434/api/generate"):
        self.model = model
        self.endpoint = endpoint

    def ask(self, prompt):
        response = requests.post(self.endpoint, json={
            "model": self.model,
            "prompt": prompt,
            "stream": True
        }, stream=True)

        print("Chatbot: ", end="", flush=True)
        for line in response.iter_lines():
            if line:
                data = line.decode("utf-8").replace("data: ", "")
                try:
                    content = eval(data).get("response", "")
                    print(content, end="", flush=True)
                except Exception:
                    pass
        print()  # nova linha após resposta completa

    def run(self):
        print("Digite sua pergunta (ou 'sair' para encerrar):")
        while True:
            user_input = input("Você: ")
            if user_input.lower() == "sair":
                break
            self.ask(user_input)
