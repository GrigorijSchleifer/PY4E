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
    """Asking user to enter the grade, check if it is a number and if it is outside the grade
    invoking the ckeck_score_validity

    Returns:
        int: Only the score as integer
    """
    while True:
        try:
            score = int(input("Your score: \n"))
            # check if the score is outside 0-1 and return False if not
            if check_score_validity(score) == True:
                print("Score is outside the range")
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
    if 0 < score > 1:
        return False
    else:
        return True

def check_grade(score_user: int) -> str:
    """Takes users score and matches it to the drade from SCORE_GRADES

    Args:
        score_user (int): _description_

    Returns:
        str: _description_
    """
    for score, grade in SCORE_GRADES.items():
        if score[0] <= score_user <= score[1]:
            return grade
        break

