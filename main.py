import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def check_for_verbose_flag(args):
    if "--verbose" in args:
        return True
    return False


def format_output(prompt, response, verbose_flag):
    print(f"User prompt: {prompt}") if verbose_flag else None
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}") if verbose_flag else None
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}") if verbose_flag else None


def main():
    try:
        user_prompt = sys.argv[1]
        verbose_flag = check_for_verbose_flag(sys.argv)
        print(f"Hello from bootdev-ai-agent!\nPrompt: {user_prompt}")
        print(verbose_flag)
        messages = [
            types.Content(
                role="user",
                parts=[types.Part(text=user_prompt)]
            )
        ]
        # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)
        print(f"User prompt: {user_prompt}") if verbose_flag else None
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}") if verbose_flag else None
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}") if verbose_flag else None
        
    except IndexError as index_error:
        print("No prompt provided.\nRun again but provide prompt. Example: uv run main.py <prompt>")
        sys.exit(1)


if __name__ == "__main__":
    main()
