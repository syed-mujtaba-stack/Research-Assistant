import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

if not OPENROUTER_API_KEY:
    print("Error: Please set the OPENROUTER_API_KEY environment variable.")
    exit(1)

def ask_openrouter(question):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    print("Welcome to the Research Assistant (OpenRouter powered)")
    while True:
        question = input("Ask a research question (or type 'exit'): ")
        if question.lower() == 'exit':
            break
        answer = ask_openrouter(question)
        print("\nAnswer:\n", answer, "\n")

if __name__ == "__main__":
    main()
