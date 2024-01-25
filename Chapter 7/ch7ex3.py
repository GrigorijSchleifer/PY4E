""" Modify the program that prompts the user for the file name so that it prints a 
“na na boo boo” if file name is “na na boo boo”. The program should behave normally 
for all other files which exist and don’t exist."""

from own_modules.ask_for_file import ask_for_filename, open_file, try_again

file_name = ask_for_filename()

def easter_egg(file_name):
    if file_name != "na na boo boo":
        print(open_file(file_name))
    else:
        print("WTF ... na na boo bo")


easter_egg(file_name)