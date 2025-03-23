import requests
import json

API_KEY = "YOUR_API_KEY"  # Replace with your Perplexity API key
API_URL = "https://api.perplexity.ai/chat/completions"

def get_response(query):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": query}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        answer = result.get("choices", [{}])[0].get("message", {}).get("content", "No answer found.")
        sources = result.get("sources", [])  # Assuming sources are included
        return answer, sources
    return "Error fetching response.", []

def main():
    print("Hello! How could I help you today? Do you have any questions regarding finance?")
    print("Please enter your question (type 'exit' to quit).")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        answer, sources = get_response(query)
        print("Bot:", answer)
        if sources:
            print("Sources:")
            for source in sources:
                print(f"- {source}")

if __name__ == "__main__":
    main()