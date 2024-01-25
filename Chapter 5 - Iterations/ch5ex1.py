# Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count, 
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.
#
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

def contin_num_print():
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
        Total: {sum(entered_nums)} 
        Sum: {len(entered_nums)}
        Average: {sum(entered_nums) / len(entered_nums)}
    """)

contin_num_print()