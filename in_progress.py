import re

# this was weired
with open('data/mbox_short.txt') as f:
    f_contents = f.readlines()
    for ln in f_contents:
        ln = ln.rstrip()
        if ln.startswith('From:'):
            # will skip lines without "From:"
            if not ln.startswith('From:'):
                continue
            print(ln)
