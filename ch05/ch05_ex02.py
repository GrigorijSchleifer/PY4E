# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

def min_max_entered_list():
    entered_nums = []
    while True:
        try:
            num = input("Enter a number ")
            if num == 'done':
                break
            num = int(num)
            entered_nums.append(num)
        except ValueError:
            print("Only integers allowed")
    print(f"""
    Min: {min(entered_nums)}
    Max: {max(entered_nums)}
    """)


min_max_entered_list()