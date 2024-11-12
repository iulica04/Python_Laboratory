# Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like Manager,
# Engineer, and Salesperson. Each subclass should have attributes like salary and methods related to their roles.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def conduct_meeting(self):
        return f"{self.name} is conducting a meeting with a team of {self.team_size} members."

    def assign_task(self, task):
        return f"{self.name} is assigning the task: {task}."

class Engineer(Employee):
    def __init__(self, name, salary, specialty):
        super().__init__(name, salary)
        self.specialty = specialty

    def develop_feature(self, feature):
        return f"{self.name} is developing the feature: {feature} in the field of {self.specialty}."

    def debug_code(self):
        return f"{self.name} is debugging the code."

class Salesperson(Employee):
    def __init__(self, name, salary, sales_made):
        super().__init__(name, salary)
        self.sales_made = sales_made

    def make_sale(self, sale_amount):
        self.sales_made += sale_amount
        return f"{self.name} made a sale of {sale_amount}."

    def report_sales(self):
        return f"{self.name} has made total sales of {self.sales_made}."

# Example usage
manager = Manager("Alice", 80000, team_size=10)
print(manager.get_details())
print(manager.conduct_meeting())
print(manager.assign_task("Complete the quarterly report"))

engineer = Engineer("Bob", 70000, specialty="Software Development")
print(engineer.get_details())
print(engineer.develop_feature("User Authentication"))
print(engineer.debug_code())

salesperson = Salesperson("Charlie", 50000, sales_made=20000)
print(salesperson.get_details())
print(salesperson.make_sale(5000))
print(salesperson.report_sales())
