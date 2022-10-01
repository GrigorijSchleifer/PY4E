"""
Reading in the Q/As, and adding Q: or A: depending on line number
Odd line numbers:       "Q: " is appendet
Non odd lien nimbers:   "A: " is appendet
"""
try:
    # r+: read and write mode
    with open("chatbot.txt", "r+") as file:
        file_object = file.readlines()
        print(type(file_object))

        for line_index in range(len(file_object)):
            line = file_object[line_index].rstrip()
            if (line_index + 1) % 2 != 0:
                print("Q: " + line, file=file_object)
            else:
                print("A: " + line, file=file_object)
except FileNotFoundError:
    print('No file found')
