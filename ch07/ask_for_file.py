def ask_for_filename():
    return input("Tell me the name of the file: ")

# data/mbox_short.txt
def open_file(file_name: str) -> str:
    """ Ask for file name and open that file, if file is missing 
    or not correct name provided, ask for another shot if Yes 
    ask for file name again, if No abort
    """ 
    # counter for specified search string
    cnt = 0 
    try:    
        with open(file_name) as f:
            f_contents = f.readlines()
        for ln in f_contents:
            ln = ln.rstrip()
            if ln.startswith('From:'):
                if not ln.startswith('From:'): continue
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

        