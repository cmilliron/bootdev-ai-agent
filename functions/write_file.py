import os

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