# Rewrite your pay computation with time-and-a-half for over time and 
# create a function called computepay which takes two parameters
# (hours and rate).

# how many hours is the regular shift 
regular_shift = 10 

def workhours_pay():
    """ Asking the user for hours worked and pay per hour
    Args:
        None
    Return:
        hours {int}: hours worked
        rate {int}: pay per hour
    """
    while True:
        try:
            hours = int(input("How many hours? \n"))
            rate = int(input("On what rate? \n"))
            break
        except ValueError:
            print("ONLY INTEGERS \n")
    return(hours, rate)

# assigning (unpacking) hour and rate 
hours, rate = workhours_pay()

# how many hours over normal shift
over_time = abs(regular_shift - hours)

def computepay(hours: int, rate: int, over_time: int) -> int:
    """ Product of hours worked * rate + over time hours (coefficient of 1.5)
    Args:
        hours {int}: hours worked
        rate {int}: rate per hour
        over_time {int}: hours worked over time
    Return:
        integer: pay with additional product of overtime mult. with a coef. of 1.5 
    """
    return(print(f"{((hours - over_time) * rate) + (over_time * (rate * 1.5))}"))

computepay(hours, rate, over_time)