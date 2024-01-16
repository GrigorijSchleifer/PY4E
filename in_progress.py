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

def calculate_pay(hours: int, pay: int, coef: float) -> None:
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
    """Call 
    """
    hours, pay = ask_for_payhourly()
    # every extra hour above 40 will be paid with a 1.5 coefficient
    extra_hours_coeff = coeff_extra_hours()
    calculate_pay(hours, pay, extra_hours_coeff)

if __name__ == "__main__":
    main()