import csv

csv_file = "students.csv"
output_file = "student_report.txt"

students = []
ages = []

with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row["Name"])
        ages.append(int(row["Age"]))

total_students = len(students)
average_age = sum(ages) / total_students if total_students > 0 else 0

with open(output_file, "w", encoding="utf-8") as file:
    file.write(f"Total Students: {total_students}\n")
    file.write(f"Average Age: {average_age:.2f}\n\n")
    file.write("Student List:\n")

    for student in students:
        file.write(f"- {student}\n")

print("Report saved to student_report.txt")
