from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


def test_get_files_info():
    print("Test 1:") 
    print(get_files_info("calculator", "."))
    print("Test 2:") 
    print(get_files_info("calculator", "pkg"))
    print("Test 3:") 
    print(get_files_info("calculator", "/bin"))
    print("Test 4:") 
    print(get_files_info("calculator", "../"))


def test_get_file_content():
    print(get_file_content("calculator", "main.py"))
    print("Test 2")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("Test 3")
    print(get_file_content("calculator", "/bin/cat"))
    print("Test 4")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


def test_write_file():
    print("Test 1:")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("Test 2:")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("Test 3:")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

def main ():
    test_write_file()


if __name__ == "__main__":
    main()
