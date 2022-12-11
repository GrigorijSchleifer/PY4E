extra_hours_ratio = 1.5

while True:
    try:
        hours = int(input("How many hour do you work? \n"))
        rate_per_hour = int(input("What is you hourly pay? \n"))
        extra_hours = int(input("How many extra hours did you work? \n"))
        break
    except ValueError:
        print('Only integers are alowed')

print(f"You will earn {(hours * rate_per_hour) + (extra_hours * extra_hours_ratio)} dollars for your shift")