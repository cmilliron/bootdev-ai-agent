import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    try:
        prompt = sys.argv[1]
        print(f"Hello from bootdev-ai-agent!\nPrompt: {prompt}")
        # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        # response = client.models.generate_content(model='gemini-2.0-flash-001', contents=prompt)
        # print(response.text)
        # print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        # print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    except IndexError as index_error:
        print("No prompt provided.\nRun again but provide prompt. Example: uv run main.py <prompt>")
        sys.exit(1)


if __name__ == "__main__":
    main()
