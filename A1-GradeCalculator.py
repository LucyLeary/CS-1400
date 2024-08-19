user_name = input("Enter your first name: ")
print("It's great to see you", user_name + "! Today we'll be figuring out what your final grade in CS 1400 might be.")
programming_assignment_score = float(input("Enter your percent grade for the programming assignments in Canvas (e.g. if you got 95% on your assignments, type 95): "))
midterm_score = float(input("Enter your cumulative grade for midterms this semester: "))
quiz_score = float(input("Enter your cumulative grade for quizzes this semester: "))
lab_score = float(input("Enter your cumulative grade for labs this semester: "))
ebook_score = float(input("Enter your cumulative grade for ebook participation this semester: "))
partial_score = .3*programming_assignment_score + .2*midterm_score + .15*quiz_score + .1*lab_score + .1*ebook_score
for count in range(0,6):
    final_exam_grade = float(count)*20
    final_grade = .15*final_exam_grade + partial_score
    print("If your final exam grade is", str(final_exam_grade) + "%, then your final grade in this class will be", str(round(final_grade)) + "%.")