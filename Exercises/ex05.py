hours = int(input("How many hours did you work today? \n"))
pay = int(input("What do you earn on an hourly bases? \n"))

# if worker does more that 40 hours
# every extra hour above 40 will be paid with a 1.5 coefficient
extra_hours_coeff = 1.5

if hours > 40: 
    pay_extra_hours = (40 * pay) + ((hours - 40) * pay) * extra_hours_coeff
    print(f"This will bring you {pay_extra_hours} per hour")
else:
    print(f"Your payroll will be {hours * pay}")