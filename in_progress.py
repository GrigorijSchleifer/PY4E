# Rewrite your pay computation with time-and-a-half for over time and 
# create a function called computepay which takes two parameters
# (hours and rate).


def working_pay_alt_intput() -> tuple:
    """ A method where first input result is not going to be deleted 
    if second input catches a ValueError exception
    Args:
        None
    Return:
        tuple (int, int): hours, pay per hour
    """
    pay_for = ["Hours", "Pay"]
    users_input = [0, 0]

    for place_input in range(len(users_input)):
        while True:
            try:
                user_input = int(input(f"{pay_for[place_input]}: "))
                # not sure if this shoul be here or after the loop
                users_input[place_input] = user_input
                print(users_input)
                break
            except ValueError:
                print("Only ingegers")
    # should be unpacked into hour and pay
    return users_input 

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

# unpacking tuple from the working_pay_alt_intput method
hours, rate = working_pay_alt_intput()
print(computepay(hours, rate, over_time(hours)))



