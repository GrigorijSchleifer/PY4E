# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted key

"""
Goal is to open a file with some text data and filter it by ':'
"""

try:
    """
    open the file, read in and replace '' tics on both ends of the line
    """
    # this is a context manager that will close the file as soon we leave the code block
    with open('data/text_to_modify.txt', 'r') as file_to_read:
        lines = file_to_read.read().split('\n')
        lines_ticks_removed = [ln.replace('\'', '', 2) for ln in lines]
except FileNotFoundError:
    print("No such file found")

with open('data/file_to_write.txt', 'w') as file_to_write:
    for ln_no_ticks in lines_ticks_removed:
        print('First part: {} and second part: {}'.format(ln_no_ticks.split(":")[0], round(float(ln_no_ticks.split(":")[1]))))







