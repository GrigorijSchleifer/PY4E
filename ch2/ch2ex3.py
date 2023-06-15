while True:
    try:
        hours = int(input("How many hour do you work? \n"))
        rate_per_hour = int(input("What is you hourly pay? \n"))
        break
    except ValueError:
        print('Only integers are alowed')

print(f"You will earn {hours * rate_per_hour} dollars for your shift")