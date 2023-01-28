import re

# this was weired
with open('data/mbox_short.txt') as f:
    f_contents = f.readlines()
    only_author = f_contents.findall(r'[Author:]\w+')
    for itm in only_author:
        print(itm, '\n')