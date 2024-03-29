# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
extra_hour_coefficient = 1.5

def ask_for_workhours() -> str:
    """Ask for hours and pay per hour

    Returns:
        hours_worked, pay_per_hour (str): both hours worked and hourly pay
    """
    while True:
        try:
            hours_worked = int(input("Hours worked \n"))
            pay_per_hour = int(input("Pay per hour \n"))
            break
        except ValueError:
            print("Only integers allowed")
    return hours_worked, pay_per_hour 

def print_hourly_pay(hours: int, pay_per_hour: int) -> str:
    """Print pay and use an elif statement to add extra hours multiplied by a coefficient 

    Args:
        hours (int): how many hours worked
        pay_per_hour (int): pay per our 

    Returns:
        str: print statemt about pay 
    """
    if hours < 40:
        print(f"Your pay: {hours * pay_per_hour}")
    elif hours > 40:
        print(f"Your pay: {(hours * pay_per_hour) + ((hours - 40) * extra_hour_coefficient)} ")

def main():
    hours, pay_per_hour = ask_for_workhours()
    return print_hourly_pay(hours, pay_per_hour)

if __name__ == "__main__":
    main()