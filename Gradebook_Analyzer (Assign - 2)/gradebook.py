
# Mini Project Assignment: GradeBook Analyzer

#------------------------------------------------------------------------------------------------------

# Course            : Programming for Problem Solving using Python
# Assignment Title  : Analysing and Reporting Student Grades
# Name              : Disha Saini
# Roll no.          : 2501730318
# Computer Science Engineering (AI & ML)
# Section           : A
# Submission Date   : 20 November 2025

#____________________________________________________________________________________________________



import csv

# ------------------------- FUNCTIONS -------------------------


# function to calculate average marks
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)


# function to calculate median marks
def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    n = len(scores)
    mid = n // 2
    if n % 2 == 1: 
        return scores[mid]
    else:
        return (scores[mid - 1] + scores[mid]) / 2


# function to calculate maximum marks
def find_max_score(marks_dict):
    return max(marks_dict.values())


# function to calculate minimum marks
def find_min_score(marks_dict):
    return min(marks_dict.values())


# function to assign particular grade to particular score values
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# ------------------------- MAIN PROGRAM LOOP -------------------------


# loop to iterate the to-do menu infinitely until user stops it
while True:

    print("=== Welcome to the GradeBook Analyzer ===")
    print("Please choose an option:")
    print("1. Enter student marks manually")
    print("2. Load student marks from a CSV file")

    choice = input("Enter option 1 or 2: ")

    marks = {}  # reset marks each run


    # --------------------- OPTION 1: MANUAL INPUT ---------------------
    if choice == "1":
        count = int(input("How many students do you want to enter? "))

        for i in range(count):   # loop to enter desired number of values of students
            name = input(f"Enter name of student {i+1}: ")
            score = int(input(f"Enter {name}'s mark: "))
            marks[name] = score

        print("\nStudent marks entered successfully!")
        print(marks)


    # --------------------- OPTION 2: CSV INPUT ------------------------
    elif choice == "2":
        filename = input("Enter the CSV filename (e.g., marks.csv): ")

        try:    # error handling
            with open(filename, 'r') as file:   # to read CSV files
                reader = csv.reader(file)
                for row in reader:
                    name = row[0]
                    score = int(row[1])
                    marks[name] = score

            print("\nCSV file loaded successfully!")
            print(marks)

        except FileNotFoundError:
            print("File not found. Please make sure the filename is correct.")
            continue  # restart loop

    else:
        print("Invalid choice. Please try again.")
        continue  # restart loop


    # --------------------- STATISTICS ------------------------
    # print statistics summary

    print("\n=== Statistics Summary ===")
    print("Average:", calculate_average(marks))
    print("Median:", calculate_median(marks))
    print("Highest mark:", find_max_score(marks))
    print("Lowest mark:", find_min_score(marks))


    # --------------------- GRADES ------------------------
 
    # assign grades based on marks 
    grades = {name: assign_grade(score) for name, score in marks.items()}


    grade_counts = {
        "A": list(grades.values()).count("A"),
        "B": list(grades.values()).count("B"),
        "C": list(grades.values()).count("C"),
        "D": list(grades.values()).count("D"),
        "F": list(grades.values()).count("F")
    }

    # print each grade and number of students with the grade
    print("\n=== Grade Distribution ===")
    for grade, count in grade_counts.items():
        print(f"{grade}: {count}")


    # --------------------- PASS / FAIL ------------------------
    # creating 2 lists of passed amd failed students respectively
    passed_students = [name for name, score in marks.items() if score >= 40]
    failed_students = [name for name, score in marks.items() if score < 40]

    # print number of students who have passed and failed
    print("\n=== Pass/Fail Summary ===")
    print(f"Passed ({len(passed_students)}): {passed_students}")
    print(f"Failed ({len(failed_students)}): {failed_students}")


    # --------------------- RESULTS TABLE ------------------------
    # print the result of all students in table format
    print("\n=== Final Results Table ===")
    print("Name\t\tMarks\tGrade")
    print("-" * 40)

    for name, score in marks.items():
        print(f"{name:<15}{score:<10}{grades[name]}")


    # --------------------- REPEAT PROGRAM ------------------------
    # to repeat or stop the program if the user chooses to
    again = input("\nWould you like to run the program again? (y/n): ")
    if again.lower() != 'y':
        print("Exiting program. Goodbye!")
        break

#-------------------------- END OF PROGRAM -------------------------