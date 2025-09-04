"""
A simple Python program to invoke OpenAI's free LLM (using the OpenAI API) and provide a response to user input.
You need to set your OpenAI API key as an environment variable named OPENAI_API_KEY.
Compatible with openai>=1.0.0
"""
import os
from openai import OpenAI

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: Please set your OPENAI_API_KEY environment variable.")
        return
    client = OpenAI(api_key=api_key)
    print("Welcome to the OpenAI LLM chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        print("LLM:", response.choices[0].message.content.strip())

if __name__ == "__main__":
    main()
