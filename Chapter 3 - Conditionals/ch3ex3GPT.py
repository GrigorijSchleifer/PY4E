# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
scores_for_grades = {
    (0.0, 0.5): "F",
    (0.51, 0.6): "E",
    (0.61, 0.7): "D", 
    (0.71, 0.8): "C",
    (0.81, 0.9): "B",
    (0.91, 1.0): "A"
}

def ask_score() -> float:
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
            print(f"Score is {score}")
            break
        except ValueError:
            print("Only integers are alowed \n")
    return score 

def find_grade(score: float) -> str:
    """Take the score from ask_score and get the grade associated with this score

    Args:
        score (float): the score from the ask_score method

    Returns:
        str: 
    """
    for range, grade in scores_for_grades.items():
        # if the score is inside the range
        if range[0] <= score <= range[1]:
            print(f"{range[0]} and {range[1]}\n")
            return grade

def print_grade(grade: str) -> str:
    """Takes the grade (ask_score -> find_grade) and prints it 

    Args:
        grade (chr): the grade from the find_grade method 

    Returns:
        chr: Prints the grade 
    """
    print(f"Your grade is: {grade}")

def main():
    print_grade(find_grade(ask_score()))

if __name__ == "__main__":
    main()
