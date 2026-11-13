def add_student():
    USN = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")
    with open("students.txt", "a") as file:
        file.write(USN + "," + name + "," + marks )
def display_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

            if len(records) == 0:
                print("No student records found.")
            else:
                print(" Student Records ")

                for record in records:
                    print(record.strip())
    except FileNotFoundError:
        print("No student records found.")


while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
