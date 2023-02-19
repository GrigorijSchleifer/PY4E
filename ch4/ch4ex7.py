# Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
#   Score   Grade
#   >= 0.9  A
#   >= 0.8  B
#   >= 0.7  C
#   >= 0.6  D
#   < 0.6   F

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