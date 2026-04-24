import os
from dotenv import load_dotenv
from google import genai

def main():
    print("Hello from ai-agent-project!")

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    question = input("prompt : ")

    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=question
    )
    print(response.text)



if __name__ == "__main__":
    main()
