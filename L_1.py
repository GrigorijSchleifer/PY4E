
# while loop with continue
while True:
    inp = input("> ")
    if inp == '#':
        print(f'first sign of the input is {inp[0]}')
        continue 
    if inp == 'done':
        print(inp)
        break
