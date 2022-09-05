condition = True

while condition:
    try:
        inp = input("type in a number")
        inp = int(inp)
        condition = False 
    except:
        print("Should be an integer")

