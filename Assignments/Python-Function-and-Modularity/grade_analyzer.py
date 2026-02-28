#Task 1 - To process scores of each students
def process_scores(students: dict) -> dict:
    student_avg_score = {}
    for student_name in students:
        total_score = sum(students[student_name])/len(students[student_name])
        student_avg_score[student_name] = round(total_score, 2)
    return(student_avg_score)

#Task 2 - Classify the grades
def classify_grades(averages: dict) -> dict:
    a = 90
    b = 75
    c = 60
    student_grades = {}
    for student_name, score in averages.items():
        if(score >= a):
            student_grades[student_name] = (score, "A")
        elif(score >= b and score < a):
            student_grades[student_name] = (score, "B")
        elif(score >= c and score < b):
            student_grades[student_name] = (score, "C")
        elif(score < c):
            student_grades[student_name] = (score, "F")
    return student_grades

#Task 3 - Generate report
def generate_report(classified: dict, passing_avg=70) -> str:
    pass_count = 0
    fail_count = 0

    print("===== Student Grade Report =====")

    for student_name in classified:
        status = "FAIL"
        avg = classified[student_name][0]
        grade = classified[student_name][1]
        if(avg >= passing_avg):
            status = "PASS"
            pass_count += 1
        else:
            fail_count += 1
        print(f"{student_name}{" "*(15-len(student_name))} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")

    print("================================") 

    return f"Total Students: {len(classified)}\nPassed        : {pass_count}\nFailed        : {fail_count}"

if __name__ == "__main__":
    students = {"Alice": [80, 95, 100, 93, 100, 75], "Bob": [94, 87, 100, 70, 40, 80], "Clara": [20, 50, 74, 60, 80, 90], "Dan": [47, 40, 50, 70, 40, 60]}
    print(generate_report(classify_grades(process_scores(students)), 60))