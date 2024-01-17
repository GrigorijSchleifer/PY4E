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
    return print(f"It is {(temp_celc * 9/5) + 32} fahrenheit")

def main():
    temp_celc = ask_for_temperature()
    convert_print_temperature(temp_celc)

if __name__ == "__main__":
    main()