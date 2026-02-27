#Function to calculate students grade
def student_grade_calculator(student_name: str, mark_1: int, mark_2: int, mark_3: int):
    total = mark_1 + mark_2 + mark_3
    percentage = (total/300)*100
    grade = ""
    if(percentage >= 75):
        grade = "A"
    elif(percentage >= 60):
        grade = "B"
    elif(percentage >= 40):
        grade = "C"
    elif(percentage < 40):
        grade = "F"
    return f"{student_name}\nTotal: {total}/300\nPercentage:{percentage:.1f}%\nGrade: {grade}"

student_name, mark_1, mark_2, mark_3 = map(lambda x: int(x) if x.isdigit() else x, input().split(", "))
print(student_grade_calculator(student_name, mark_1, mark_2, mark_3))