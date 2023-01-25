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
    with open('data/text_to_modify.txt', 'r') as file_to_read:
        lines = file_to_read.read().replace('\'', '', 4).split('\n')
        for ln in lines:
            lines_ticks_removed = ln.replace('\'', '', 2)
except FileNotFoundError:
    print("No such file found")

# with open('data/file_to_write.txt', 'w') as file_to_write:
#     for line in range(0, len(lines)):
#         print(f"For {lines[line].split(':')[0]} the Type of the second input is: {type(lines[line].split(':')[1])}")

# Hey Ho from iPad
with open('data/file_to_write.txt', 'w') as file_to_write:
    for ln_no_ticks in lines_ticks_removed:
            print('First part: {} and second part: {}'.format(ln_no_ticks.split(":")[0], ln_no_ticks.split(":")[0]))