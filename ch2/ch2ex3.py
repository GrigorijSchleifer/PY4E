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
    


if __name__ == "__main__":
    main()