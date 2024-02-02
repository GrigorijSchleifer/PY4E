# Exercise 3: Write a program to prompt for a score_range between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

import data.constants as constants

# dictionary containing score range and corresponding grade
SCORE_AND_GRADES = constants.SCORE_AND_GRADES

def ask_score_range() -> float:
    """Write a program to prompt for a score_range betwween 0.0 and 1.0. If the score is out of range print an error message. 
    If the score_range is between 0.0 and 1.0 print a grade using the following table. 

    Returns:
        int: _description_
    """
    while True:
        try:
            score = float(input("What was your score? \n"))
            if not 0 <= score <= 1: 
                print("Score must to be between 0 and 1 \n")
                continue
            break
        except ValueError:
            print("Only integers are alowed \n")
    return score 

def find_grade(user_score: float) -> str:
    """Take the score_range from ask_score and get the grade associated with this score

    Args:
        score_range (float): the score from the ask_score method

    Returns:
        str: 
    """
    for range_score, grade in SCORE_AND_GRADES.items():
        # if the score_range is inside the range
        if range_score[0] <= user_score <= range_score[1]:
            return grade

def print_grade(grade: str) -> str:
    """Takes the grade (ask_score_range -> find_grade) and prints it 

    Args:
        grade (chr): the grade from the find_grade method 

    Returns:
        chr: Prints the grade 
    """
    print(f"Your grade is: {grade}")

def main():
    user_score = ask_score_range()
    grade = find_grade(user_score)
    print_grade(grade)

if __name__ == "__main__":
    main()




















