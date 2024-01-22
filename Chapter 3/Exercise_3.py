# Exercise 3: Write a program to prompt for a score_range between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
SCORE_FOR_GRADES = {
    (0.0, 0.5): "F",
    (0.51, 0.6): "E",
    (0.61, 0.7): "D", 
    (0.71, 0.8): "C",
    (0.81, 0.9): "B",
    (0.91, 1.0): "A"
}

def ask_score_range() -> float:
    """Write a program to prompt for a score_range betwween 0.0 and 1.0. If the score is out of range print an error message. 
    If the score_range is between 0.0 and 1.0 print a grade using the following table. 

    Returns:
        int: _description_
    """
    while True:
        try:
            score = float(input("What was your score? \n"))
            if score < 0 or score > 1:
                print("score_range has to be between 0 and 1 \n")
                continue
            break
        except ValueError:
            print("Only integers are alowed \n")
    return score 

def find_grade(range: float) -> str:
    """Take the score_range from ask_score and get the grade associated with this score

    Args:
        score_range (float): the score from the ask_score method

    Returns:
        str: 
    """
    for range_score, grade in SCORE_FOR_GRADES.items():
        # if the score_range is inside the range
        if range_score[0] <= range <= range_score[1]:
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




















