def ask_for_filename():
    """This method asking for users input and will be (?invoked?) 
    Args: 
    Return: 
    """
    return input("Tell me the name of the file: ")


# data/mbox_short.txt
def open_file(file_name: str) -> str:
    """ Ask for file name and open that file, if file is missing 
    or name not correct provided, ask for another shot if Yes ask for file name again, if No abort
    """ 
    # counter for specified search string
    cnt = 0 
    try:    
        with open(file_name) as f:
            f_contents = f.readlines()
        for ln in f_contents:
            # removing white space and blank lines
            ln = ln.rstrip()
            if not ln.startswith('From:'): 
                continue
            cnt = cnt + 1
    except:
        print("File cannot be found")
        try_again()
    return f'There are {cnt} lines that start with \'From:\''

def try_again():
    yes_or_no = input('Do you want another shot?')
    if yes_or_no.lower() == 'yes':
        open_file(ask_for_filename())
    else:
        exit()


def open_file_find_method(file_name: str) -> str:
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


def try_again():
    yes_or_no = input('Do you want another shot?')
    if yes_or_no.lower() == 'yes':
        open_file(ask_for_filename())
    else:
        exit()


def ch07_11_ex_2(file_name: str) -> str:
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