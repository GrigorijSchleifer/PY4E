# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
scores_for_grades = {
    (0,0, 0,5): "F",
    (0.51, 0.6): "E",
    (0.61, 0.7): "D", 
    (0.71, 0.8): "C",
    (0.81, 0.9): "B",
    (0.91, 1.0): "A"
}

def ask_score(grade = None) -> int:
    """Write a program to prompt for a score betwween 0.0 and 1.0. If the score is out of range print an error message. 
    If the score is between 0.0 and 1.0 print a grade using the following table. 

    Returns:
        int: _description_
    """
    while True:
        try:
            score = float(input("What was your score? \n"))
            if score < 0 or score > 1:
                print("Score has to be between 0 and 1 \n")
                continue
            print(f"Inside the try block the score is {score}")
            break
        except ValueError:
            print("Only integers are alowed \n")
    print(score)
    return grade

def print_score():
    score = ask_score()
    return print(f"Your score is {score}")


print_score()


























age_group = {
    (0.0, 18.0): "Kids",
    (18.1, 30.0): "Yound adults",
    (30.1, 50.0): "Adults",
    (50.1, 65.0): "Elderly",
    (65.1, float("inf")): "Old"
}

def what_age_group(age: int) -> chr:
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
    
print(f"Based on your age, you are: {what_age_group(age_group)}")
