from student import Student

if __name__ == '__main__':
    student = Student('Evgeny', 'Vladimirovich', 'Lobachev', 'subj.csv')

    student.add_test_score("Math", 63)
    student.add_test_score("Math", 93)
    student.add_grade("Math", 4)

    student.add_test_score("Russian", 82)
    student.add_test_score("Russian", 50)
    student.add_test_score("Russian", 84)
    student.add_grade("Russian", 4)

    student.add_test_score("English", 94)
    student.add_grade("English", 5)

    print(f'Средний бал тестов по математике: {student.average_test_score("Math"):.1f}')
    print(f'Средний бал тестов по русскому языку: {student.average_test_score("Russian"):.1f}')
    print(f'Средний бал тестов по физике: {student.average_test_score("English"):.1f}')
    print(f'Средняя оценка по всем предметам: {student.average_grade():.1f}')