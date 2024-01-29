# Rewrite your pay computation with time-and-a-half for over time and 
# create a function called computepay which takes two parameters
# (hours and rate).

def asking_pay_and_hours() -> tuple:
    """ Alternative method using a list to be filled with users input 
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
                # this is needed because otherwise Pay will be asked indefinitely
                break
            except ValueError:
                print("Only integers")
        users_input[place_input] = user_input
    # should be unpacked into hour and pay
    return users_input 

def calculate_overtime(hours: int) -> int:
    """Returns the number of hours worked beyond 8 hours per shift.
    Args:
        hours (int): Hours worked from the asking_pay_and_hours method

    Returns:
        int: Returns the number of hours worked beyond 8 hours per shift.
    """
    regular_shift = 8
    return abs(regular_shift - hours)

def computepay(hours: int, rate: int) -> int:
    """ Product of hours worked * rate + over time hours (coefficient of 1.5)
    Args:
        hours {int}: hours worked
        rate {int}: rate per hour
    Return:
         
    """
    return f"{((hours - calculate_overtime(hours)) * rate) + (calculate_overtime(hours) * (rate * 1.5))}"

def main():
    hours, rate = asking_pay_and_hours()
    print(computepay(hours, rate))

if __name__ == "__main__":
    main()

