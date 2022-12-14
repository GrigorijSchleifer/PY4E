# Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. 
# If the score isbetween 0.0 and 1.0, print a grade using the following table:
#   Score     Grade
#   >= 0.9    A
#   >= 0.8    B
#   >= 0.7    C
#   >= 0.6    D
#   < 0.6     F

while True:
    try:
        score = float(input("What was your score? \n"))
        if score < 0 or score > 1:
            print("Score has to be between 0 and 1 \n")
            continue
        break
    except ValueError:
        print("Only integers are alowed \n")

def score_grader(score, grade = None):
    if score >= 0.9:
        grade = "A" 
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    elif score < 0.6:
        grade = "F"
    return grade

print(f'Your score is {score_grader(score, grade=None)}')
