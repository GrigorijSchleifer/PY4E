import re

def open_file(fl_name: str) -> str:
    # this was weired
    with open(fl_name) as f:
        fl_name = input("Tell me the name of the file: ")
        f_contents = fl_name.readlines()
        cnt = 0
        for ln in f_contents:
            ln = ln.rstrip()
            if ln.startswith('From:'):
                if not ln.startswith('From:'): continue
                cnt = cnt + 1
    return f'There are {cnt} lines that start with \'From:\''

def try_again():
    yes_or_no = input('Do you want another shot?')
    if yes_or_no.lower() == 'yes':
        open_file()
try:
    print(open_file(fl_name))
except:
    print("File cannot be found")
    exit()

