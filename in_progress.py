age_group = {
    (0.0, 18.0): "Kids",
    (18.1, 30.0): "Yound adults",
    (30.1, 50.0): "Adults",
    (50.1, 65.0): "Elderly",
    (65.1, float("inf")): "Old"
}

def what_age_group(ages: dict) -> chr:
    """Based on users age what age group he/she is? 
    Args:
        dict: dictionary of age categories and corresponding groups
    Return:
        chr: Text output in what grade user will be"""
    while True:
        try:
            age = float(input("Your age: \n"))
            if age < 0:
                print("Too young")
                continue
            for age_range, group in ages.items():
                if age_range[0] <= age <= age_range[1]:
                    return group
        except ValueError:
            print("Only intgers are allowed")
        # looping over categories and finding the group user is in
    
print(f"Based on your age, you are a {what_age_group(age_group)}")