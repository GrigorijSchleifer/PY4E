import re

# this was weired
with open('data/mbox_short.txt') as f:
<<<<<<< HEAD
    f_contents = f.readlines()
    cnt = 0
    for ln in f_contents:
        count =+ 1 
        print(count) 
=======
    f_contents = f.read()
    pattern = "Author:"

    print(re.search(pattern, f_contents))
>>>>>>> 40f889609803303f0ec1cb780b2e07f150ac9228
