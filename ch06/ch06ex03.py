# Encapsulate this code in a function named count, and generalize 
# it so that it accepts the string and the letter as arguments.

count = 0

def ask_for_word():
    while True:
        try:
            inp = str(input('What word should we scan for a string?'))
            if inp == 'done':
                break
        except ValueError:
            print('This is not a string')
    return inp

def ask_for_char():
    while True:
        try:
            count_char = str(input('What character should we count?'))
            if count_char == 'done':
                break
        except ValueError:
            print('Not a character')
        return count_char

def count_char(word, chr, count):
    print(word)
    print(chr)
    for i in word:
        if i == chr:
            count += 1
    return count

print(count_char(ask_for_word(), ask_for_char(), count))
