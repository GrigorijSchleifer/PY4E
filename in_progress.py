# gamma calculator
from typing import List, Any

dct_ctlms = {}

def ask_catecholamins(dct: dict) -> str:
    """ Asking for catecholamins and flowrates to fill the dct_ctlms  

    Returns:
        str: _description_
    """  
    while True:
        try:
            ctlm = input("What catecholamins are running? \n")
        except ValueError:
            print("Only characters are allowed")
        
        # assign None value to a catecholamine
        # None will be raplaces in ask_rate()
        dct[ctlm] = None

        # exiting the loop
        if ctlm.lower() == 'exit':
            break
    
    return dct 

def ask_rate() -> str:
    """_summary_

    Returns:
        str: _description_
    """    
    return None

def dspl_ctlms() -> str:
    """Function asking user for the running catecholamins
    
    Args:
        no arguments, user will provide them into the ctlms dictionary

    Return"
        ctlms (str): dictionary filled with catecholamins and infusion rate

    """
    return None

# use ask_catecholamins to fill the dct_ctlms dict with catecholamins and flowrates
print(ask_catecholamins(dct_ctlms))