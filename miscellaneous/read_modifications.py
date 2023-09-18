import readline


with open('chatbot.txt') as chb:
    chb_chars = chb.readlines()

print(chb_chars[:10])

line_number = 0

for line in chb_chars:
    # strip new line character from the end of the line
    line = line.rstrip()
    if line.startswith("Warum "):
        print(line)

# a different way to thing about the loop
for line in chb_chars:
    line = line.rstrip()
    if not line.startswith("Warum"):
        continue
    else:
        print(line)

# printing only questions
for line in chb_chars:
    line = line.rstrip()
    if not "?" in line:
        continue
    else:
        print(line)
