import os, subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to execute. Required. Relative to the working directory."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(full_path).startswith((os.path.abspath(working_directory))):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if os.path.basename(full_path).split(".")[1] != "py":
        return f'Error: "{file_path}" is not a Python file.'
    # print(subprocess.run("pwd", capture_output=True, cwd=os.path.abspath(working_directory)))
    try:
        result = subprocess.run(
            ["uv", "run", full_path, *args], 
            capture_output=True, 
            timeout=30, 
            # cwd=os.path.abspath(working_directory)
            )
        output_string = f"Output:\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}\n"
        if result.returncode != 0:
            output_string = output_string + f"Process exited with code {result.returncode}"
        # if len(result) == 0:
        #     return "No Output produced"
        return output_string
    except Exception as e:
        return f"Error: executing Python file: {e}"