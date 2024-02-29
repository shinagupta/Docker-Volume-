def save_student_name(name):
    with open("student.txt", "a") as file:
        file.write(name + "\n")

def show_all_students():
    try:
        with open("student.txt", "r") as file:
            students = file.readlines()
            if not students:
                print("No student names recorded yet.")
            else:
                print("List of Student Names:")
                for student in students:
                    print(student.strip())
    except FileNotFoundError:
        print("No student names recorded yet.")

def main():
    while True:
        print("\nOptions:")
        print("1. Enter Student Name")
        print("2. Show All Students")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            student_name = input("Enter the student name: ")
            save_student_name(student_name)
            print(f"Student name '{student_name}' saved successfully.")
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__":
    main()
