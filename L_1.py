
# while loop with continue
while True:
    inp = input("> ")
    if inp == '#':
        print(f'first sign of the input is {inp[0]}')
        continue 
    if inp == 'done':
        print(inp)
        break


# codewars first method for chaining
def fct_one(x): 
    return x * 10
def fct_two(x): 
    return x * 10

functions_list = [fct_one, fct_two]


def chain(value, functions: list) -> int:
    """
    Chaining funcitions and use the returned value 
    in the next called function

    Args: List of functions 
    return: Integer as a result of both function calls   
    """
    for i in functions:
        value = i(value)
    return print(value)

chain(100, functions_list)


# funcition to find largest number in a list
lst = [10, 10, 10, 10, 10, 10, 10]

def largest_number(l: list) -> int:
    """
    Function to find largest number in a list
    
    Args: list

    return: number
    """
    max_num = 0

    for itm in l:
        if itm > max_num:
            max_num = itm
    return max_num 


def sum_list(l: list) -> int:
    """
    Taking in a list and summing up all items 

    Args: list

    return: integer
    """
    sum_lst = 0
    for itm in l:
        sum_lst += itm 
    return sum_lst 

sum_list(lst)



def avg_list(l: list) -> int:
    """
    Taking in a list and summing up all items 

    Args: list

    return: integer
    """
    sum_lst = 0
    for itm in l:
        sum_lst += itm 
        return sum_lst / len(l)

avg_list(lst)