import csv

class Staff:
    def __init__(self, staff_id, name, phone_number, email, role):
        self.id = staff_id
        self.name = name
        self.phoneNumber = phone_number
        self.email = email
        self.role = role  # Boolean attribute to indicate role (True for manager, False for employee)

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"Email: {self.email}")
        print(f"Role: {'Manager' if self.role else 'Employee'}")  # Display role based on boolean value


class Manager(Staff):
    def __init__(self, staff_id, name, phone_number, email, manage_group, employee_count, total_revenue):
        super().__init__(staff_id, name, phone_number, email, True)  # Set role to True for manager
        self.manageGroup = manage_group
        self.employeeCount = employee_count
        self.totalRevenue = total_revenue

    def display_info(self):
        super().display_info()
        print(f"Manage Group: {self.manageGroup}")
        print(f"Employee Count: {self.employeeCount}")
        print(f"Total Revenue: ${self.totalRevenue}")


class Employee(Staff):
    def __init__(self, staff_id, name, phone_number, email, revenue, working_month_count):
        super().__init__(staff_id, name, phone_number, email, False)  # Set role to False for employee
        self.revenue = revenue
        self.workingMonthCount = working_month_count

    def display_info(self):
        super().display_info()
        print(f"Revenue: ${self.revenue}")
        print(f"Working Month Count: {self.workingMonthCount}")
