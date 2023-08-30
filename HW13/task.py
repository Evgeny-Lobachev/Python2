from name_exeptions import StudentNameError, InvalidScoreError, InvalidSubjectError
from student import Student

try:
    student = Student("Евгений Лобачев", "subj.csv")
    student.add_score("Math", 5)
    student.add_test_result("Math", 94)
    print(student.average_test_score("Math"))
    print(student.average_score())

except InvalidSubjectError as e:
    print("Error:", e)

except StudentNameError as e:
    print("Error:", e)

except InvalidScoreError as e:
    print("Error:", e)