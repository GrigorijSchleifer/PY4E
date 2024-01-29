# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
# method for askin a temerature
def ask_for_temperature():
    """Asking for temperature

    Returns:
        temp (float): float number representing temperature in celcius 
    """
    while True:
        try:
            temp = float(input("What is the temperature? "))
            break
        except ValueError:
            print("Only integers allowed")
    return temp


def convert_print_temperature(temp_celc: float) -> str:
    """Taking a celius temperature, converting in f. and printing it

    Args:
        temp_celc (float): celsius as a floag

    Returns:
        str: printing fahrenheit number after converting from celsius
    """
# method for converting and printing
    return (temp_celc * 9/5) + 32 

def print_temperature(temp_fahr):
    """Takes the string of the temperature in fahrenheit and prints it

    Args:
        temp_fahr (str): temperature in fahrenheit 

    Returns:
        str: printed message that displays the temperature in fahrenheit
    """
    return print(f"It is {temp_fahr} fahrenheit")

def main():
    temp_celc = ask_for_temperature()
    temp_fahr = convert_print_temperature(temp_celc)
    print_temperature(temp_fahr)
    
if __name__ == "__main__":
    main()