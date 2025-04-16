programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def getGrade(Mark) :
    if Mark >= 91 :
        return "Outstanding"
    elif Mark >= 81 :
        return  "Exceeds Expectations"
    elif Mark >= 71 :
        return "Acceptable"
    else :
        return "Fail"
student_grades = dict ([[student, getGrade(student_scores[student])] for student in student_scores])
print(student_grades)