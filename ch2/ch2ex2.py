print(f"First module is {__name__}")

def get_user_name():
    """
    write a program that uses input to prompt a user for their name and then welcomes them.  
    args: 
        no arguments
    return:
        str: users name
    """
    inp = input("what is your name ?\n")
    return inp

def greet_user(name: str) -> str:
    """
    greets user by their name
    Args:
        str: string name from the get_user_name method
    returns:
        str: _description_
    """
    return print(f"Hello {name}")

def main():
    user_name = get_user_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()
