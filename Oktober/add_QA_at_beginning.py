"""
Reading in the Q/As, and adding Q: or A: depending on available "?"

"""
try:
    # r+: read and write mode
    with open("chatbot.txt", "r+") as f:
        for line in f:
            print(line) 
except FileNotFoundError:
    print('No file found')
