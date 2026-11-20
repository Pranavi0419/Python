print("STUDENT MARKS CALCULATOR")

name = input("Enter student name: ")

mark1 = int(input("Enter subject 1 marks: "))
mark2 = int(input("Enter subject 2 marks: "))
mark3 = int(input("Enter subject 3 marks: "))

total = mark1 + mark2 + mark3

average = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")

elif average >= 75:
    print("Grade: B")

elif average >= 50:
    print("Grade: C")

else:
    print("Grade: Fail")