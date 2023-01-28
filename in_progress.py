# this was weired
with open('data/mbox_short.txt') as f:
    f_contents = f.readlines()
    for itm in f_contents:
        print(itm, '\n')