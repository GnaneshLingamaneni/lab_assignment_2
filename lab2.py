class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return "{} {} {} {}".format(self.emp_id, self.name, self.age, self.salary)

def sort_employees(employees, sort_parameter):
    if sort_parameter == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sort_parameter == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sort_parameter == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")
        return employees

def print_employees(employees):
    for emp in employees:
        print(emp)

if __name__ == "__main__":
    employees = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000)
    ]

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    try:
        sort_parameter = int(input("Enter your choice (1/2/3): "))
        sorted_employees = sort_employees(employees, sort_parameter)
        print("\nSorted Employee Data:")
        print_employees(sorted_employees)
    except ValueError:
        print("Invalid input. Please enter a number.")
