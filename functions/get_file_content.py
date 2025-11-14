import os
# from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(full_path).startswith((os.path.abspath(working_directory))):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(full_path, "r") as f:
        content = f.read(10000)
    if len(content) == 10000:
        return f"{content[:10000]}...file \"{os.path.basename(file_path)}\""
    return content

def main():
    print(get_file_content("calculator", "main.py"))
    print("Test 2")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("Test 3")
    print(get_file_content("calculator", "/bin/cat"))
    print("Test 4")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()