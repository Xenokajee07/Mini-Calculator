print("📘 Welcome to the Muslim School Grade Reporter")

def get_student_data():
    students = []
    count = int(input("How many students? "))

    for i in range(count):
        name = input(f"Enter name of student #{i+1}: ")
        mark = float(input(f"Enter mark for {name}: "))
        students.append((name, mark))

    return students

def analyze_data(students):
    total = 0
    highest = students[0]
    lowest = students[0]

    for name, mark in students:
        total += mark
        if mark > highest[1]:
            highest = (name, mark)
        if mark < lowest[1]:
            lowest = (name, mark)

    average = total / len(students)

    return average, highest, lowest
students = get_student_data()
average, highest, lowest = analyze_data(students)

print("\n📊 Grade Summary")
print("------------------------")
print("Average:", round(average, 2))
print("Highest:", highest[0], "→", highest[1])
print("Lowest:", lowest[0], "→", lowest[1])
def write_report(students, average, highest, lowest):
    with open("grade_report.txt", "w") as file:
        file.write("📘 STUDENT GRADE REPORT\n")
        file.write("------------------------\n")
        for name, mark in students:
            file.write(f"{name}: {mark}\n")

        file.write("\nSUMMARY\n")
        file.write(f"Average: {round(average, 2)}\n")
        file.write(f"Highest: {highest[0]} → {highest[1]}\n")
        file.write(f"Lowest: {lowest[0]} → {lowest[1]}\n")
write_report(students, average, highest, lowest)
print("\n📂 Report has been saved to 'grade_report.txt'")


