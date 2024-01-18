# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

def hour_and_rate() -> str:
    """Ask user for hours worked and pay rate per hour
    Returns:
        str: Returns hours of work and pay per hour 
    """
    while True:
        try:
            hours = int(input("how many hour do you work? \n"))
            rate_hour = int(input("What is you hourly pay? \n"))
            break
        except ValueError:
            print("Only integers allowed")
    return hours, rate_hour

def print_gross_pay(hours, rate_hour):
    """Printing the total 
    Args:
        hours (str): how many hours worked  
        rate_hour (str): pay per hour 
    """
    print(f"You will earn {hours * rate_hour} dollars")

def main():
    hours, rate_hour = hour_and_rate()
    print_gross_pay(hours, rate_hour)
    
if __name__ == "__main__":
       main()


def ask_for_payhourly() -> int:
    """Asking for hour worked and pay per our
    Ags:
        No arguments
    Return:
        Integers for hours worked and pay per hour are returned
    """
    while True:
        try:
            hours = int(input("How many hours did you work today? \n"))
            pay = int(input("What do you earn on an hourly bases? \n"))
            break
        except ValueError:
            print("Only integers please")
    return hours, pay

def coeff_extra_hours():
    """Asking for coefficient for extra hours worked
    Args:
        no args
    Return:
        coeff_extra_hours (int): coefficient to multiply wiht for every extra hour
    """
    while True:
        try:
            # every extra hour above 40 will be paid with a 1.5 coefficient
            coeff_extra_hour = float(input("How many extra hours?"))
            break
        except ValueError:
            print("Only integers allowed")
    return coeff_extra_hour

def print_pay(hours: int, pay: int, coef: float) -> None:
    """Calculation amd printing pay per hour
    Args:
        hours (int): how many hours were worked
        pay (int): pay per hour
        coeff (float): every extra hour above 40 will be paid with a coefficient from coeff_extra_hours
    Return:
        String: print calculated pay
    """
    if hours > 40:  
        print(f"This will bring you {(40 * pay) + ((hours - 40) * pay) * coef} per hour")
    else:
        print(f"Your payroll will be {hours * pay}")

def main():
    """Collect worked hours and pay per hour firs, than ask for a coefficient and multiply every hour after 40 with that coefficient 
    Args:
    Return:
        str: no return but print statement of the pay
    """
    hours, pay = ask_for_payhourly()
    # every extra hour above 40 will be paid with a 1.5 coefficient
    extra_hours_coeff = coeff_extra_hours()
    print_pay(hours, pay, extra_hours_coeff)

if __name__ == "__main__":
    main()
