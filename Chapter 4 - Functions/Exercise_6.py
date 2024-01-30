# rewrite your pay computation with time-and-a-half for over time and 
# create a function called computepay which takes two parameters
# (hours and rate).

def asking_pay_and_hours() -> tuple:
    """ alternative method using a list to be filled with users input 
    args:
        none
    return:
        tuple (int, int): hours, pay per hour
    """
    pay_for = ["hours", "pay"]
    users_input = [0, 0]

    for place_input in range(len(users_input)):
        while True:
            try:
                user_input = int(input(f"{pay_for[place_input]}: "))
                # this is needed because otherwise pay will be asked indefinitely
                break
            except ValueError:
                print("only integers")
        users_input[place_input] = user_input
    # should be unpacked into hour and pay
    return users_input 

def calculate_overtime(hours: int) -> int:
    """returns the number of hours worked beyond 8 hours per shift.
    args:
        hours (int): hours worked from the asking_pay_and_hours method

    returns:
        int: returns the number of hours worked beyond 8 hours per shift.
    """
    regular_shift = 8
    return abs(regular_shift - hours)

def computepay(hours: int, rate: int) -> int:
    """ product of hours worked * rate + over time hours (coefficient of 1.5)
    args:
    hours {int}: hours worked
    rate {int}: rate per hour
    return:
    """
    return f"{((hours - calculate_overtime(hours)) * rate) + (calculate_overtime(hours) * (rate * 1.5))}"

def main():
    hours, rate = asking_pay_and_hours()
    print(computepay(hours, rate))

if __name__ == "__main__":
    main()

