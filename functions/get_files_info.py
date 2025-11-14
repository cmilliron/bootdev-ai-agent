import os

def get_files_info(working_directory, directory="."):
    if not isinstance(directory, str):
        return f'Error: "{directory}" is not a directory'
    full_path = os.path.join(working_directory, directory)
    print(full_path)
    print(os.path.abspath(working_directory))
    if not os.path.abspath(full_path).startswith((os.path.abspath(working_directory))):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    try:
        files_list = os.listdir(full_path)
        output_string = ""      
        for file in files_list:
            file_path = os.path.join(full_path, file)
            file_size = os.path.getsize(file_path) # Get the size of a file
            is_file = os.path.isfile(file_path) # Check if a path is a file
            output_string = output_string + f"- {file}: filesize={file_size}, is_dir={not is_file}\n"
    except Exception as error:
        return f"Error: {error}"
    return output_string


def main():
    print(get_files_info("calculator",  "."))

if __name__ == "__main__":
    main()