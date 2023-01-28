import re

# this was weired
with open('data/mbox_short.txt') as f:
    f_contents = f.readlines()
    only_author = re.findall(r'[Author:]\w+', f_contents)
    for itm in only_author:
        print(itm, '\n')