def collect_input():
    """
    Asking user for a number, if input is not a number,
    catching eception and returning to the input prompt

    Args: no arguments
    Return: computated average of values in the list
    """
    lst = list()
    try:
        while True:
            input_variable = input("Your input: \n\n Type \"done\" for exit \n")
            if input_variable == 'done': break
            lst.append(int(input_variable))
    except ValueError:
        print("Only integers are allowed! ")
        collect_input()
    return print(f"We have the list: {lst} with the average {sum(lst)/len(lst)}")

collect_input()
