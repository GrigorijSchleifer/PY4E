with open('chatbot.txt') as chb:
    chb_chars = chb.readlines()

print(chb_chars[:10])

line_number = 0

for line in chb_chars:
    if line.startswith("Warum "):
        print(line)


