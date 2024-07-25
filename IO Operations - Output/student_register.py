

student_num = int(input("Please enter the number of students: "))

with open('reg_form.txt', 'w') as f:
    f.write(2 * "\n" + 5 * "=" + "Student Register" + 5 * "=" + 3 * "\n")
    for student in range(0,student_num):
        studentID = input("Please enter student ID: ")
        f.write(str(studentID + " " + 10 * "." + "\n"))
