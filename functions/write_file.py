import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file at a specified location, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read content from. must be provided."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to be written or overwriting to a file, relative to the working directory.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(full_path).startswith((os.path.abspath(working_directory))):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(os.path.dirname(full_path)):
        os.makedirs(full_path)
    with open(full_path, "w") as f:
        f.write(content)    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

def main():
    write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    write_file("calculator", "/tmp/temp.txt", "this should not be allowed")   

if __name__ == "__main__":
    main()