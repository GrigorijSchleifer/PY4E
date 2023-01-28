import re

# this was weired
with open('data/mbox_short.txt') as f:
    f_contents = f.readlines()
    pattern = "Author:"

    print(re.search(pattern, itm))