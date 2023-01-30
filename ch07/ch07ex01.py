import re

def open_file(fl_name: str) -> str:
    # this was weired
    with open(fl_name) as f:
        f_contents = f.readlines()
        cnt = 0
        for ln in f_contents:
            ln = ln.rstrip()
            if ln.startswith('From:'):
                if not ln.startswith('From:'): continue
                cnt = cnt + 1
    return f'There are {cnt} lines that start with \'From:\''
    

try:
    fl_name = input("Tell me the name of the file: ")
    print(open_file(fl_name))
except:
    print("File cannot be found")
    exit()