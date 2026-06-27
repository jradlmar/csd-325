grades = []

print("Student Grade Average Calculator")
print("Enter grades from 0 to 100.")
print("Type 'done' when you are finished.")

while True:
    user_input = input("Enter a grade or type 'done': ")

    if user_input.lower() == "done":
        break

    try:
        grade = float(user_input)

        if grade < 0 or grade > 100:
            print("Invalid grade. Please enter a number between 0 and 100.")
        else:
            grades.append(grade)
            print("Grade added.")

    except ValueError:
        print("Invalid input. Please enter a number or type 'done'.")

if len(grades) == 0:
    print("No grades were entered.")
else:
    average = sum(grades) / len(grades)

    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print("Grades entered:", grades)
    print("Average grade:", round(average, 2))
    print("Letter grade:", letter_grade)
