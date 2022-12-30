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
    #  
    while len_string != 0:
        print(string_from_input[len_string - 1])
        len_string -= 1    

def input_string() -> str:
    while True:
        try:
            input_string = str(input("Input: ")) 
            if input_string == "done":
                break
            else:
                inverse_string(input_string)
        except ValueError:
            print("Bad input")

input_string()



