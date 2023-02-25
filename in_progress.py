file_for_modification = "data/mbox_short.txt"

def open_file_here(file_name: str) -> str:
    with open(file_name) as f:
        f = f.readlines()
        for ln in f:
            ln = ln.rstrip()
            if not ln.startswith('X-DSPAM-Processed:'): 
                continue
            words = ln.split()
            print(words[2])

open_file_here(file_for_modification)