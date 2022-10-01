def collect_input():
    """
    Asking user for a number, if input is not a number,
    catching eception and returning to the input prompt
    """
    try:
        while True:
            input_variable = input("Your input: \n\n Type \"done\" for exit \n")
            if input_variable == 'done': break
    except ValueError:
        print("Only integers are allowed! ")
        collect_input()

try:
    collect_input()
except ValueError:
    print('Input has to be an integer')
