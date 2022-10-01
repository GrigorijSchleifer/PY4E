try:
    with open("chatbot.txt") as file_object:
        file_object = file_object.readlines()
except FileNotFoundError:
    print('No file found')

for line_index in range(len(file_object)):
    line = file_object[line_index].rstrip()
    if (line_index + 1) % 2 != 0:
        print("Q: " + line)
    else:
        print("A: " + line)
        

