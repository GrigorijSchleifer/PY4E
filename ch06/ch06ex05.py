# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted hey
# hellow from the web editor!

"""
Goal is to open a file with some text data and filter it by ':'
"""

try:
    with open('text_to_modify.txt', 'r') as file_to_read:
        lines = file_to_read.read().split('\n')
except FileNotFoundError:
    print("No such file found")

with open('file_to_write.txt', 'w') as file_to_write:
    for line in range(0, len(lines)):
        print(f"For {line.split(':')[0]} the rounded integer is {lines.split(':')[1]}")








