print("📊 Welcome to the Grade Analyzer")

# Step 1: Get marks input
marks_input = input("Enter student marks separated by commas (e.g. 67,80,45,90): ")

# Step 2: Convert input string into a list of numbers
marks_list = marks_input.split(",")

print("Student Marks:", marks_list)
# Step 3: Convert string list to number list
marks = []
for mark in marks_list:
    marks.append(float(mark))
print("Converted Marks:", marks)
# Step 4: Analyze the marks
total_students = len(marks)
total_marks = sum(marks)
average = total_marks / total_students
highest = max(marks)
lowest = min(marks)
print("📈 Total Students:", total_students)
print("📊 Average Mark:", average)
print("🏆 Highest Mark:", highest)
print("🔻 Lowest Mark:", lowest)
# Step 5: Determine pass and fail counts
passes = 0
fails = 0

for mark in marks:
    if mark >= 50:
        passes += 1
    else:
        fails += 1

print("✅ Passed:", passes)
print("❌ Failed:", fails)
print("\n📋 FINAL REPORT")
print("----------------------")
print("Total Students:", total_students)
print("Average Mark: ", round(average, 2), "%")
print("Highest Mark: ", highest)
print("Lowest Mark:  ", lowest)
print("✅ Passes:     ", passes)
print("❌ Fails:      ", fails)
