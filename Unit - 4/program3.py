import csv

try:
    n = int(input("Enter number of employees: "))

    with open("payroll.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Employee ID", "Name", "Basic Salary",
                         "Allowance", "Deduction", "Net Salary"])

        for i in range(n):
            print("\nEnter Employee", i + 1, "Details:")

            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            basic = float(input("Enter Basic Salary: "))
            allowance = float(input("Enter Allowance: "))
            deduction = float(input("Enter Deduction: "))

            net_salary = basic + allowance - deduction

            writer.writerow([emp_id, name, basic, allowance,
                             deduction, net_salary])

        print("\nPayroll saved successfully!")

    with open("payroll.csv", "r") as file:
        reader = csv.reader(file)

        print("\n--- Employee Payroll Records ---")

        for row in reader:
            print(" | ".join(row))

except ValueError:
    print("Error: Please enter valid numeric values.")

except FileNotFoundError:
    print("Error: File not found.")
