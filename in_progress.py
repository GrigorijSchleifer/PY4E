# where is vimrc for v
# where should I store my venv's
from ch07.ask_for_file import ask_for_filename, try_again
import re

f_name = ask_for_filename()

def ch07_11_ex_2(file_name: str) -> str:
    """Read through the file and look for "X-DSPAM-Confidence: 0.8475", if encountered
    pull apart the line and extract the floating-point number. Count these lines and then 
    compute the total of the spam confidence

    Args: name of the file
    Return: A string with lines containing the string
    """
    floats = []
    try:
        with open(file_name) as f:
            f_contents = f.readlines()
            for ln in f_contents:
                ln = ln.rstrip()
                # if the resutl is -1 (X-DSPAM-Confidence) not found
                if ln.find("X-DSPAM-Confidence") == -1: 
                    continue
                else:
                    floats.append(float(re.split(":", ln)[1]))
    except:
        print("File not found")
        try_again()
    return f"The floats average is {sum(floats)/len(floats)}"

print(ch07_11_ex_2(f_name))
