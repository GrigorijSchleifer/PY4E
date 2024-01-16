while True:
    try:
        degree_celsius = float(input("How cold is it outside in celsius? \n"))
        print(f"I is {(degree_celsius * 9/5) + 32} fahrenheit!")
        break
    except ValueError:
        print("Only floats please")
