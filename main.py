import os
from dotenv import load_dotenv
from google import genai

def main():
    print("Hello from ai-agent-project!")

    load_dotenv() 

    api_key = os.environ.get("GEMINI_API_KEY") # collect the api key
    client = genai.Client(api_key=api_key)
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    print(f"User prompt: {prompt}")

    response = client.models.generate_content( # generate de answer using the model specified
        model='gemini-2.5-flash', contents=prompt
    )

    usage_metadata = response.usage_metadata # collect the meta information (including tokens infos)
    prompt_token = usage_metadata.prompt_token_count # number of tokens for the prompt
    response_token = usage_metadata.candidates_token_count # number of tokens for the answer

    print(f"Prompt tokens: {prompt_token}\nResponse tokens: {response_token}")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
