# Jared Morris
# Module 8 Assignment
# JSON Student List Program

import json


def print_students(student_list):
    """Print each student in the required format."""
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )


def main():
    filename = "Student.json"

    # Load the JSON file into a Python list.
    with open(filename, "r", encoding="utf-8") as file:
        students = json.load(file)

    print("This is the original Student list:")
    print_students(students)

    # Add Jared Morris to the student list.
    new_student = {
        "F_Name": "Jared",
        "L_Name": "Morris",
        "Student_ID": 99999,
        "Email": "jmorris@gmail.com"
    }
    students.append(new_student)

    print("\nThis is the updated Student list:")
    print_students(students)

    # Save the updated list back to the JSON file.
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

    print("\nThe Student.json file was updated.")


if __name__ == "__main__":
    main()
