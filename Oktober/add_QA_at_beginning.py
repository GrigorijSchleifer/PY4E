"""
open a file in read mode (only string is returned)
create a new file in write mode and use the string from the first file
to write lines into the second file
"""
try:
    with open('chatbot.txt', 'r') as file_to_read:
        file_read = file_to_read.read().rstrip()
        # split the string file we just read in on \n
        file_read_split = file_read.split("\n")
except FileNotFoundError():
    print("No such file found")

with open('file_to_write.txt', 'w') as file_to_write:
    # file_read_trimmed = file_read.rstrip()

for line in file_read_trimmed:
    print(line)