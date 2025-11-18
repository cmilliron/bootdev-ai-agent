import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python_file import run_python_file, schema_run_python_file
from prompts import system_prompt
import pprint

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)

function_dictionary = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
}

def call_functions(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    if function_call_part.name not in function_dictionary:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    else:
        function_response = function_dictionary[function_call_part.name](working_directory="./calculator", **function_call_part.args)
        print(function_response)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_response},
                )
            ],
        )


def check_for_verbose_flag(args):
    if "--verbose" in args:
        return True
    return False


def format_output(prompt, response, verbose_flag):
    print(f"User prompt: {prompt}") if verbose_flag else None
    print("Verbose: ", response.text)
    (
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        if verbose_flag
        else None
    )
    (
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        if verbose_flag
        else None
    )


def main():
    try:
        user_prompt = sys.argv[1]
        verbose_flag = check_for_verbose_flag(sys.argv)
        print(f"Hello from bootdev-ai-agent!\nPrompt: {user_prompt}")
        # print(verbose_flag)
        messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
        # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )
        # pprint.pprint(response.function_calls)
        print(f"User prompt: {user_prompt}") if verbose_flag else None
        if response.function_calls != None:
             # print(response.function_calls)
            for item in response.function_calls:
                 # print(f"Calling function: {item.name}({item.args})")
                call_functions(item,  verbose=True)
        else:
            print("Response:", response.text)
        if verbose_flag:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    except IndexError as index_error:
        print(
            "No prompt provided.\nRun again but provide prompt. Example: uv run main.py <prompt>"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
