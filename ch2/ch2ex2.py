# ch2ex1
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

    returns:
        str: _description_
    """
    users_name = get_users_name()
    return print(f"hello {users_name}")

def main():
    user_name = get_user_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()