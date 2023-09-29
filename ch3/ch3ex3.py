# Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
#   Score     Grade
#   >= 0.9    A
#   >= 0.8    B
#   >= 0.7    C
#   >= 0.6    D
#   < 0.6     F

scores_for_grades = {
    (0,0, 0,5): "F",
    (0.51, 0.6): "E",
    (0.61, 0.7): "D", 
    (0.71, 0.8): "C",
    (0.81, 0.9): "B",
    (0.91, 1.0): "A"
}

def score_grader(grade = None):
    while True:
        try:
            score = float(input("What was your score? \n"))
            if score < 0 or score > 1:
                print("Score has to be between 0 and 1 \n")
                continue
            break
        except ValueError:
            print("Only integers are alowed \n")

    if score >= 0.9:
        grade = "A" 
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"
    return grade

print(f'Your score is {score_grader(grade=None)}')

age_group = {
    (0.0, 18.0): "Kids",
    (18.1, 30.0): "Yound adults",
    (30.1, 50.0): "Adults",
    (50.1, 65.0): "Elderly",
    (65.1, float("inf")): "Old"
}


def what_class_for_age(ages: dict) -> chr:
    """Based on users age what class will be attended
    Args:
        dict: dictionary of age categories and corresponding grades
    Return:
        chr: Text output in what grade user will be"""
    while True:
        try:
            age = float(input("Your age: \n"))
            if age < 0:
                print("Too young")
                continue
        except ValueError:
            print("Only intgers are allowed")
    
        
