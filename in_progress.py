# Exercise 2: Figure out which line of the above program is still not
# properly guarded. See if you can construct a text file which causes the
# program to fail and then modify the program so that the line is properly
# guarded and test it to make sure it handles your new text file.

# create a heuristic for defining the second argument for the open() method
# make an infinite loop to ask for the second argument of open() and quiting user wants to
# guard the ln.split() line in case the file is opened as binary not pure text.
def return_mode(argument):
    argument = {

    }

def argument_for_open():
    try:
        print("""Choose the mode for the open method:
        1: read
        2: write
        3: binary
        """)
        inp_mode = int(input("Your choice: \n"))
        # limit the input to number between 1 - 3
        if inp_mode in range(1, 3):
            return 
        else:
            print("Pleas choose the option 1-2")
    except ValueError:
        print("Only integers allowed")
        argument_for_open()
    return inp_mode



# argument_for_open() will prompt user to define the mode for the open method
with open('data/mbox_short.txt', str(argument_for_open())) as fhand:
    for ln in fhand:
        words_splitonly = ln.split()
        if len(words_splitonly) == 0: continue
        # print(f"Words only: {words_splitonly}")
        if words_splitonly[0] != 'From': continue
        print(f"Another words: {words_splitonly[2]}")

