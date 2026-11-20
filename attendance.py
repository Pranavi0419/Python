
name = input("Enter student name: ")
total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter attended classes: "))

if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
    print("Please enter valid attendance details.")
else:
    percentage = (attended_classes / total_classes) * 100

    print("\nStudent Attendance Report")
    print("Name:", name)
    print("Attendance:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Status: Eligible for exams")
    else:
        print("Status: Not eligible for exams")
