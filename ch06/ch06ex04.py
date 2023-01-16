# Exercise 4: There is a string method called count that is similar to 
# the function in the previous exercise. Read the documentation of this

# Method at: https://docs.python.org/library/stdtypes.html#string-methods

# Wriii an invocation that counts the number of times the letter a occurs
# in “banana”

def check_if_done(done):
    return True if done == 'done' else False

def word_to_count():
    words_for_counting = []
    while True:
        try:
            words_for_counting.append(str(input('What word do you want \n')))
            if check_if_done(words_for_counting[-1]) == True:
                break
        except ValueError:
            print('Only strings')
    return words_for_counting[len(words_for_counting)-2]

print(word_to_count().count('a'))