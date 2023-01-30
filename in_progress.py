import re

with open('data/mbox_short.txt') as f:
    f_contents = f.readlines()
    for ln in f_contents:
        ln = ln.rstrip()
        if ln.startswith("From:"):
            print(ln)

