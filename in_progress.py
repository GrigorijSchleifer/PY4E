import re

# this was weired
with open('data/mbox_short.txt') as f:
    f_contents = f.readlines()
    rgx = re.compile(r'[\Author:]')

    for itm in f_contents:
        if re.search(rgx, itm):
            print(itm)