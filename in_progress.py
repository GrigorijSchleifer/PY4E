# Exercise 2: Figure out which line of the above program is still not
# properly guarded. See if you can construct a text file which causes the
# program to fail and then modify the program so that the line is properly
# guarded and test it to make sure it handles your new text file.

# create a heuristic for defining the second argument for the open() method
# make an infinite loop to ask for the second argument of open() and quiting user wants to
# guard the ln.split() line in case the file is opened as binary not pure text.
def argument_for_open():
    try
with open('data/mbox_short.txt') as fhand:
    for ln in fhand:
        words_splitonly = ln.split()
        if len(words_splitonly) == 0: continue
        # print(f"Words only: {words_splitonly}")
        if words_splitonly[0] != 'From': continue
        print(f"Another words: {words_splitonly[2]}")

