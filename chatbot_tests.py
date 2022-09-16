chb = open('chatbot.txt')
chb_chars = chb.read()

line_number = 0

for line in chb:
   line_number += 1 
    
print(line_number)
print(len(chb_chars))
print(chb_chars[:20])

