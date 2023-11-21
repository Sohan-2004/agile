class Employee:
    def __init__(self, emp_id, name, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary

# Sample employee data
employees = [
    Employee(1, 'John Doe', 'IT', 'Software Engineer', 60000),
    Employee(2, 'Jane Smith', 'HR', 'HR Manager', 75000),
    # ... more employees
]
def display_menu():
    print("1. View all employees")
    print("2. Add new employee")
    print("3. Remove employee")
    # ... other options

def view_all_employees():
    for emp in employees:
        print(f"ID: {emp.emp_id}, Name: {emp.name}, Dept: {emp.department}, Designation: {emp.designation}, Salary: {emp.salary}")

def add_employee(emp_id, name, department, designation, salary):
    new_emp = Employee(emp_id, name, department, designation, salary)
    employees.append(new_emp)
    print("Employee added successfully!")

def remove_employee(emp_id):
    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            print("Employee removed successfully!")
            break
    else:
        print("Employee not found!")
def login(username, password):
    # Check credentials in the database or hardcoded
    if username == 'admin' and password == 'admin123':
        return True
    else:
        return False

# Usage
username = input("Enter username: ")
password = input("Enter password: ")
if login(username, password):
    display_menu()
    choice = int(input("Enter your choice: "))
    # Handle user choice
else:
    print("Invalid credentials")
import json

# Save employee data to a file
def save_employees():
    with open('employees.json', 'w') as file:
        json.dump([emp.__dict__ for emp in employees], file)

# Load employee data from a file
def load_employees():
    try:
        with open('employees.json', 'r') as file:
            data = json.load(file)
            employees.clear()
            for emp in data:
                employees.append(Employee(**emp))
    except FileNotFoundError:
        pass  # File not found initially
