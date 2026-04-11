

import requests

API_KEY = ""  # Replace with your actual Groq API key

def ask_bot(question):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",  # Updated working model
        "messages": [
            {"role": "system", "content": "You are a helpful medical assistant. Give safe and general advice only. Always remind users to consult a doctor for serious medical issues."},
            {"role": "user", "content": question}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        
        # Print debug info if error
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            return
            
        result = response.json()
        
        print("\n🤖 Health Assistant:", result['choices'][0]['message']['content'])
        print("\n" + "-"*50)
        
    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
    except KeyError as e:
        print(f"API Response Error: {e}")
        print("Response content:", response.text if 'response' in locals() else "No response")

# Run chatbot
print("="*50)
print("🏥 Welcome to Health Assistant Chatbot")
print("="*50)
print("Note: I provide general health information only.")
print("Always consult a doctor for serious medical concerns.")
print("Type 'quit' or 'exit' to end the conversation.")
print("="*50 + "\n")

while True:
    q = input("❓ Ask Health Question: ")
    
    if q.lower() in ['quit', 'exit', 'bye']:
        print("\n👋 Stay healthy! Goodbye!")
        break
    
    if not q.strip():
        print("Please enter a valid question.\n")
        continue
    
    ask_bot(q)