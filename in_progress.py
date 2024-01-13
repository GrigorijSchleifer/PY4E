print(__name__)

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






# # gamma calculator
# from typing import List, Any

# dct_ctlms = {}

# def ask_catecholamins(dct: dict) -> str:
    # """ asking for catecholamins and flowrates to fill the dct_ctlms  

    # returns:
        # str: _description_
    # """  
    # while true:
        # try:
            # ctlm = input("what catecholamins are running? \n")
        # except valueerror:
            # print("only characters are allowed")
        
        # # assign none value to a catecholamine
        # # none will be raplaces in ask_rate()
        # dct[ctlm] = none

        # # exiting the loop
        # if ctlm.lower() == 'exit':
            # break
    
    # return dct 

# def ask_rate() -> str:
    # """_summary_

    # returns:
        # str: _description_
    # """    
    # return none

# def dspl_ctlms() -> str:
    # """function asking user for the running catecholamins
    
    # args:
        # no arguments, user will provide them into the ctlms dictionary

    # return"
        # ctlms (str): dictionary filled with catecholamins and infusion rate

    # """
    # return none

# # use ask_catecholamins to fill the dct_ctlms dict with catecholamins and flowrates
# print(ask_catecholamins(dct_ctlms))