def ask_for_payhoury() -> int:
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

# assign hours worked and pay per hour  
hours, pay = ask_for_payhoury()

# every extra hour above 40 will be paid with a 1.5 coefficient
extra_hours_coeff = 1.5

def calculate_pay(hours: int, pay: int, coef: float) -> None:
    """Calculation amd printing pay per hour
    Args:
        hours: how many hours were worked
        pay: pay per hour
        coeff: every extra hour above 40 will be paid with a 1.5 coefficient 
    Return:
        String: Calculated pay
    """
    if hours > 40: 
        pay_extra_hours = (40 * pay) + ((hours - 40) * pay) * coef
        print(f"This will bring you {pay_extra_hours} per hour")
    else:
        print(f"Your payroll will be {hours * pay}")

calculate_pay(hours, pay, extra_hours_coeff)