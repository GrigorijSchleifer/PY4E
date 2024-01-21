# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
scores_for_grades = {
    (0,0, 0,5): "F",
    (0.51, 0.6): "E",
    (0.61, 0.7): "D", 
    (0.71, 0.8): "C",
    (0.81, 0.9): "B",
    (0.91, 1.0): "A"
}

def ask_users_score(grade = None) -> int:
    """Write a program to prompt for a score betwween 0.0 and 1.0. If the score is out of range print an error message. 
    If the score is between 0.0 and 1.0 print a grade using the following table. 

    Returns:
        int: _description_
    """
    while True:
        try:
            score = float(input("What was your score? \n"))
            # this is not really smart and should be handled differently
            # better to check if score is higher 0 and lower 1 and break if True
            # but it is nice to see how the keyword "continue" is used inside a try block
            if score < 0 or score > 1:
                print("Score has to be between 0 and 1 \n")
                continue
            break
        except ValueError:
            print("Only integers are alowed \n")
    return score

def print_score():
    score = ask_users_score()
    return print(f"Your score is {score}")


print_score()




