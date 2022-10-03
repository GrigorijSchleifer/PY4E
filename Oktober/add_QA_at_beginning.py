"""
Reading in the Q/As, and adding Q: or A: depending on available "?"

"""
try:
    # r+: read and write mode
    with open("chatbot.txt", "r+") as f:
        for line in f:
            line = line.rstrip()
            if line.endswith("?"):
                f.write(f'Q: {line}') 
            else:
                f.write(f'A: {line}')
except FileNotFoundError:
    print('No file found')



with open("chatbot.txt", "r+") as ff:
    size_to_read = 10

    text_chunk = ff.read(size_to_read)
    while len(text_chunk) > 0:
        print(text_chunk, end='*')
        text_chunk = ff.read(size_to_read)