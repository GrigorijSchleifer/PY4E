import re

# this was weired
with open('data/mbox_short.txt') as f:
    f_contents = f.read()
    pattern = "Author:"

    print(re.search(pattern, f_contents))