# Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

def inverse_string(string_from_input: str) -> str:
    """ Taking users input from input_sting method and returning that strings inverse version
    Args: 
        String from the input_string method
    Return:
        Sting that is coming from the input_sting method, but reversed
    """

    len_string = len(string_from_input)

    # print all characters of the input string in reverse order 
    reversed_str = ""

    while len_string != 0:
        reversed_str += string_from_input[len_string-1]
        len_string -= 1    
    return reversed_str

def input_string() -> str:
    while True:
        try:
            input_string = str(input("Input: ")) 
            if input_string == "done":
                break
            else:
                inversed_string = inverse_string(input_string)
        except ValueError:
            print("Bad input")
        return inversed_string

# activating both method to ask for input and reverse it
print(input_string())




