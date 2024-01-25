"""Exercise 1: Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements."""

lst = ["Das", "ist", "sehr", "sehr", "cool"]

def chop(lst: list) -> None:
    """Function takes a list and modifies it, removing the first and last elements, and 
        returns None
    
    Args: 
        param1 (list): list that will be sliced

    Returns: 
        None
    """
    lst_chop = []
    # new variable is needed to prevent adding ["ist"] to lst
    lst = lst_chop.append(lst[1:len(lst)-1])
    return lst

def middle(lst: list) -> list:
    """Function takes a list and modifies it, removing and returning all but first and last element.
    
    Args: 
        param1 (list): list that will be sliced

    Returns: 
        All items except first and last
    """
    middle_lst = []
    # for itm in range(1, len(lst)-1):
        # print(lst[itm])
    return [lst[itm] for itm in range(1, len(lst)-1)]

print(middle(lst))