# Rewrite your pay computation with time-and-a-half for over time and 
# create a function called computepay which takes two parameters
# (hours and rate).

def workhours_pay() -> tuple:
    """ Asking the user for hours worked and pay per hour
    Args:
        None
    Return:
        tuple (int, int): hours, pay per hour
    """
    while True:
        try:
            hours = int(input("How many hours? \n"))
            rate = int(input("On what rate? \n"))
            break
        except ValueError:
            print("ONLY INTEGERS \n")
    # no brackets needed 
    return hours, rate

# how many hours over normal shift
def over_time(hours: int) -> int:
    regular_shift = 8
    return regular_shift - hours

# return time was incorrect 
def computepay(hours: int, rate: int, over_time: int) -> int:
    """ Product of hours worked * rate + over time hours (coefficient of 1.5)
    Args:
        hours {int}: hours worked
        rate {int}: rate per hour
        over_time {int}: takes the over_time function to return hours worked over time
    Return:
        
    """
    # amazing!!! all without brackets and ""
    # no printed object should be returned
    return f"{((hours - over_time) * rate) + (over_time * (rate * 1.5))}"

# assigning (unpacking) hour and rate
# no brackets needed!!! 
hours, rate = workhours_pay()

computepay(hours, rate, over_time())


# In terms of the workhours_pay() function:
# - you should be able to return hours, pay without the need for the brackets. They will be a tuple by default
# - the docstring for return is incorrect. you are returning a tuple. it should be `Returns: tuple(int, int): hours, pay per hour 
# with computerpay, it is bad practice to include print statements in a function. Functions should return something - in this case, i would just return the string that you have constructed.
# the reason we don't use print statements in functions generally is that once it has run the data is lost, and to get it back, you need to run again, whereas if you run it and a varaible with the outputs, it can be printed many times, or saved or something else
# i don't think you need abs for your calculation of overtime. This just gets an absolyte numbers (for example, abs(20) and abs(-20) both return 20)
# i think here you were trying to remove the minus if this came into play. This is a way of doing it but I personally would just have done this as a function
# my personal preference though and not necessarily a criticism
# finally, functions should be defined at the top and called at the bottom.
# other than that, all great! well done!!