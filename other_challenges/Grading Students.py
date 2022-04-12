def gradingStudents(grades):
    result_arr = []
    for grade in grades:
        if(grade >= 38):
            if (5 - (grade % 5)) < 3:
                grade = 5 - (grade % 5) + grade
        result_arr.append(grade)
    return result_arr
print(gradingStudents([73, 67, 38, 33]))