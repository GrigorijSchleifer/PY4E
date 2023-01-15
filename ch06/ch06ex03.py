# Encapsulate this code in a function named count, and generalize 
# it so that it accepts the string and the letter as arguments.

# the count of characters to look for will be stored here
count = 0

def check_if_done(inpt):
    """ 
    Checking if the user wants to quit the loop and enters 'done'

    Args:       string from the user
    
    Return:     Boolean, if the input was 'done', the input of
                ask_for_word and ask_for_chat will be stoped
    """
    done_or_not = False

    if inpt == 'done':
        done_or_not = True
    else:
        done_or_not = False
    return done_or_not 

def ask_for_word():
    while True:
        try:
            inp = str(input('What word should we scan for a string? \n'))
            if check_if_done(inp) == False:
                break
        except ValueError:
            print('This is not a string')
    return inp

def ask_for_char():
    while True:
        try:
            count_char = str(input('What character should we count? \n'))
            if check_if_done(count_char) == False:
                break
        except ValueError:
            print('Not a character')
    return count_char

def count_char(word, chr, count):
    for i in word:
        if i == chr:
            count += 1
    return count

print(count_char(ask_for_word(), ask_for_char(), count))
