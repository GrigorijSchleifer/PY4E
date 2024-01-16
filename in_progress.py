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