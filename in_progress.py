"""Exercise 1: Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements."""
lst = ["Das", "ist", "cool"]

# token updated
def chop(lst: list) -> None:
    lst = lst.append(lst[1:len(lst)-1])
    return lst



print(chop(lst))