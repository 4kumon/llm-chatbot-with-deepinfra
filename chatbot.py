import requests
import json

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
                try:
                    data = json.loads(line.decode("utf-8").removeprefix("data: "))
                    token = data.get("response", "")
                    print(token, end="", flush=True)
                except Exception as e:
                    continue
        print()  # nova linha ao final da resposta

    def run(self):
        print("Digite sua pergunta (ou 'sair' para encerrar):")
        while True:
            user_input = input("Você: ")
            if user_input.lower() == "sair":
                break
            self.ask(user_input)
