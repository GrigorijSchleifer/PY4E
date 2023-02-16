# where is vimrc for v
from ch07.ask_for_file import ask_for_filename, try_again

f_name = ask_for_filename()

def ch07_11_ex_1(file_name: str) -> str:
    """A separate method to try out the find method and to help understand 
    what -1 means if string is not found

    Args: name of the file
    Return: A string with lines containing the string
    """
    cnt = 0
    try:
        with open(file_name) as f:
            f_contents = f.readlines()
            for ln in f_contents:
                ln = ln.rstrip()
                if ln.find('From:') == -1: continue
                print(ln.upper())
    except:
        print("File not found")
        try_again()

ch07_11_ex_1(f_name)