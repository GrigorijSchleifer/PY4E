# Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
#   Score   Grade
#   >= 0.9  A
#   >= 0.8  B
#   >= 0.7  C
#   >= 0.6  D
#   < 0.6   F

SCORE_GRADES = {
    (1.0, 0.9): 'A',
    (0.89, 0.8): 'B',
    (0.79, 0.7): 'C', 
    (0.69, 0.6): 'D',
    (0.59, 0.0): 'F'
}

def ask_for_score() -> int:
    """Asking user to enter the grade, checks if "grade" is a number and is outside the ranges of SCORE_GRADE ckeck_score_validity 

    Returns:
        int: Only the score as integer
    """
    while True:
        try:
            score = float(input("Your score: \n"))
            # check if the score is outside 0-1 and return False if not
            if check_score_validity(score) == True:
                break
        except ValueError:
            print("Only integers allowed")
    return score

def check_score_validity(score: int) -> bool:
    """If the score is outside 0-1 range method returns False

    Args:
        score (int): users score from the ask_for_score method

    Returns:
        bool: If False is returned while loop in ask_for_score() askes another score
    """
    if not 0 <= score <= 1:
        print(f"{score} is outside the range")
        return False
    else:
        return True

def assign_grade(score_user: float) -> str:
    """Takes users score and matches it to the drade from SCORE_GRADES

    Args:
        score_user (int): _description_

    Returns:
        str: _description_
    """
    print(f"The score we recieved is {score_user}")

    for score_range, grade in SCORE_GRADES.items():
        print(f"score range: {score_range}, users_score: {score_user}, grade: {grade}")

        if score_range[0] <= score_user <= score_range[1]:
            print(f"THE grade is : {grade}")
        return grade

def print_grade_msg(grade: str) -> str:
    print(f"The grade is {grade}")

if __name__ == "__main__":
    user_score = ask_for_score()
    grade = assign_grade(user_score)
    print_grade_msg(grade)
