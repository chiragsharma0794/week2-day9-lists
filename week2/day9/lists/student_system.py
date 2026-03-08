records = [
    ["Aman", "Math", 88],
    ["Priya", "Physics", 91],
    ["Rahul", "Math", 76],
    ["Sneha", "Chemistry", 85],
    ["Karan", "Physics", 79],
    ["Neha", "Math", 95],
    ["Arjun", "Chemistry", 89],
    ["Simran", "Physics", 84],
    ["Vikas", "Math", 67],
    ["Pooja", "Chemistry", 92]
]

def add_student(name, subject, marks):
    for record in records:
        if record[0].lower() == name.lower() and record[1].lower() == subject.lower():
            print("Duplicate record found. Student with same name and subject already exists.")
            return
    records.append([name, subject, marks])
    print("Student added successfully.")

def get_toppers(subject):
    subject_records = [record for record in records if record[1].lower() == subject.lower()]
    toppers = sorted(subject_records, key=lambda x: x[2], reverse=True)[:3]
    return toppers

def class_average(subject):
    marks_list = [record[2] for record in records if record[1].lower() == subject.lower()]
    if not marks_list:
        return 0
    return sum(marks_list) / len(marks_list)

def above_average_students():
    if not records:
        return []
    overall_average = sum(record[2] for record in records) / len(records)
    return [record for record in records if record[2] > overall_average]

def remove_student(name):
    global records
    before_count = len(records)
    records = [record for record in records if record[0].lower() != name.lower()]
    removed_count = before_count - len(records)
    if removed_count > 0:
        print(f"{removed_count} record(s) removed for student '{name}'.")
    else:
        print("Student not found.")

def save_to_file():
    with open("students.txt", "w") as file:
        for record in records:
            file.write(f"{record[0]}, {record[1]}, {record[2]}\n")
    print("Records saved to students.txt")

def show_all_records():
    if not records:
        print("No student records available.")
        return
    print("\nCurrent Student Records:")
    for index, record in enumerate(records, start=1):
        print(f"{index}. Name: {record[0]}, Subject: {record[1]}, Marks: {record[2]}")

def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. Show toppers")
        print("3. Show class average")
        print("4. Show above-average students")
        print("5. Remove student")
        print("6. Show all records")
        print("7. Pop last student record")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ").strip()
            subject = input("Enter subject: ").strip()
            try:
                marks = int(input("Enter marks: "))
                add_student(name, subject, marks)
            except ValueError:
                print("Invalid marks. Please enter an integer.")

        elif choice == "2":
            subject = input("Enter subject: ").strip()
            toppers = get_toppers(subject)
            if toppers:
                print(f"Top 3 students in {subject}:")
                for topper in toppers:
                    print(topper)
            else:
                print("No records found for this subject.")

        elif choice == "3":
            subject = input("Enter subject: ").strip()
            avg = class_average(subject)
            if avg == 0:
                print("No records found for this subject.")
            else:
                print(f"Average marks in {subject}: {avg:.2f}")

        elif choice == "4":
            students = above_average_students()
            if students:
                print("Students scoring above overall class average:")
                for student in students:
                    print(student)
            else:
                print("No above-average students found.")

        elif choice == "5":
            name = input("Enter student name to remove: ").strip()
            remove_student(name)

        elif choice == "6":
            show_all_records()

        elif choice == "7":
            if records:
                removed = records.pop()
                print("Last record removed using pop():", removed)
            else:
                print("No records to pop.")

        elif choice == "8":
            save_to_file()
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
    