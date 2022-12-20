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
    return abs(regular_shift - hours)

# return time was incorrect 
def computepay(hours: int, rate: int, over_time: int) -> int:
    """ Product of hours worked * rate + over time hours (coefficient of 1.5)
    Args:
        hours {int}: hours worked
        rate {int}: rate per hour
        over_time {int}: takes the over_time function to return hours worked over time
    Return:
         
    """
    return f"{((hours - over_time) * rate) + (over_time * (rate * 1.5))}"

hours, rate = workhours_pay()
print(computepay(hours, rate, over_time(hours)))




