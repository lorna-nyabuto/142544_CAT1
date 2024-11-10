class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")
    
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to {self.salary}.")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added employee {employee.name} (ID: {employee.employee_id}) to {self.department_name} department.")
    
    def calculate_total_salary_expenditure(self):
        total_salary = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure for {self.department_name} department is: ${total_salary}")
        return total_salary
    
    def display_all_employees(self):
        if self.employees:
            print(f"Employees in {self.department_name} department:")
            for emp in self.employees:
                emp.display_details()
        else:
            print(f"No employees in the {self.department_name} department.")


department = Department("Engineering")

employee1 = Employee("Lorna Nyabuto", "L001", 70000)
employee2 = Employee("Nicole Kirimi", "N002", 80000)

print("---- Employee and Department Management System ----")
department.add_employee(employee1)
department.add_employee(employee2)

department.display_all_employees()

employee1.update_salary(75000)

department.calculate_total_salary_expenditure()
