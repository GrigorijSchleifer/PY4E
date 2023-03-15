# Exercise 2: Figure out which line of the above program is still not
# properly guarded. See if you can construct a text file which causes the
# program to fail and then modify the program so that the line is properly
# guarded and test it to make sure it handles your new text file.
3
# create a heuristic for defining the second argument for the open() method
# make an infinite loop to ask for the second argument of open() and quiting user wants to
# guard the ln.split() line in case the file is opened as binary not pure text.
def input_error_generator(inp) -> str:
    """Evaluating users input and printing the error message 
    Args: 
        Whatever is typed in by the user
    Return:
        Str: Error message
    """
    # limit the input to number between 1 - 3
    if inp in range(1, 2):
        print(return_mode(inp))
        return return_mode(inp_mode)
    else:
        print(f"{inp_mode} cannot be used. Please choose the option 1-2 \n")
        argument_for_open() 


def return_mode(argument: int) -> int:
    """Users input from argument_for_open()
    Args: 
        Integer: between 1 - 3 representing the mode a file should be opened in
    Return:
        String: describing how you want the file to be opened
    """
    argument_dict = {
        1: 'r',
        2: 'b'
    }
    return argument_dict.get(argument)

def argument_for_open():
    try:
        print("""Choose the mode for the open method:
        1: read
        2: binary
        """)
        inp_mode = int(input("Your choice: "))
        
    except ValueError:
        print(f"{inp_mode} cannot be used. Please choose the option 1-2 \n")
        argument_for_open()



# argument_for_open() will prompt user to define the mode for the open method
with open('data/text_to_modify.txt', argument_for_open()) as fhand:
    for ln in fhand:
        print(ln)
        words_splitonly = ln.split()
        print(words_splitonly)
        if len(words_splitonly) == 0: continue
        # print(f"Words only: {words_splitonly}")
        if words_splitonly[0] != 'X-DSPAM-Confidence': continue
        print(f"Another words: {words_splitonly[1]}")

