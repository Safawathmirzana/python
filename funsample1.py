def average(marks):
    sum_mark=sum(marks)
    total_subjects=len(marks)
    average_mark=sum_mark/total_subjects
    return average_mark
def total_grade(average_mark):
    if average_mark >= 80:
        grade='A'
    elif average_mark >= 60:
        grade='B'
    elif average_mark >= 50:
        grade='c'
    else:
        grade='F'
    return grade  
mark=[55,65,75,80,65]
average_mark=average(mark)
grade=total_grade(average_mark)
print("your average mark is: ",average_mark)
print("your grade is :",grade)
