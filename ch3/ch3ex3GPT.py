def score_grader():
    # Define a dictionary of score ranges and grades
    grades = {
        (0.9, 1.0): "A",
        (0.8, 0.9): "B",
        (0.7, 0.8): "C",
        (0.6, 0.7): "D",
        (0.0, 0.6): "F"
    }

    # Ask the user for the score and validate it
    while True:
        try:
            score = float(input("What was your score? \n"))
            if 0 <= score <= 1:
                break
            else:
                print("Score has to be between 0 and 1 \n")
        except ValueError:
            print("Only integers are allowed \n")

    # Loop through the dictionary and find the matching grade
    for range, grade in grades.items():
        if range[0] <= score < range[1]:
            print(f"{range[0]} and {range[1]}\n")
            return grade

# Call the function and print the result
print(score_grader())

def enter_restr_byage() -> chr:
    """Ask user for age and print message in what age group and if allowed to enter
    Args:
        No arguments
    Return:
        Character"""

    # dict with ages the user will be assigned to
    age_group = {
        (0, 18): "Young",
        (19, 65): "Adults", 
        (66, 100): "Oldies"
    }
    while True:
        try:
            age_user = int(input("What is you age? \n"))
            break
        except ValueError:
            print("Only integers are allowed")

    # loop ove3r age groups and find corresponding group wher the user is located
    for age, group in age_group.items():
        if age[0] <= age_user <= age[1]:
            print(f"You are in {group} group")