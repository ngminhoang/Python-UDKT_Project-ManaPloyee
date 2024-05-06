import csv
from models import *

class DataTable:
    def __init__(self):
        self.data = []
        self.load_data("data/data.csv")

    def load_data(self, csv_file):
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.data.append(row)

    def get_data(self):
        return self.data
    
    def save_data(self):
        with open("data/data.csv", 'w', newline='') as file:
            fieldnames = self.data[0].keys() if self.data else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

    def delete_record_by_id(self, record_id):
        updated_data = [record for record in self.data if record.get('ID') != record_id]
        self.data = updated_data
        self.save_data()

    def add_row(self, obj):
        if isinstance(obj, Employee):
            new_record = {
                'ID': obj.id,
                'Name': obj.name,
                'Phone Number': obj.phoneNumber,
                'Email': obj.email,
                'Role': 0,
                'Revenue': obj.revenue,
                'Working Month Count': obj.workingMonthCount
            }

        elif isinstance(obj, Manager):
            new_record = {
                'ID': obj.id,
                'Name': obj.name,
                'Phone Number': obj.phoneNumber,
                'Email': obj.email,
                'Role': 1,
                'Manage Group': obj.manageGroup,
                'Employee Count': obj.employeeCount,
                'Total Revenue': obj.totalRevenue
            }
        else:
            raise ValueError("Unsupported object type. Expected Employee or Manager.")

        # Append new record to internal data
        self.data.append(new_record)

        # Append new record to CSV file
        fieldnames = self.data[0].keys() if self.data else new_record.keys()
        with open("data/data.csv", 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header if file is empty
            if not self.data:
                writer.writeheader()

            # Write new record to CSV file
            writer.writerow(new_record)

    def search_row_by_id(self, id):
        updated_data = [record for record in self.data if record.get('ID') == id]
        self.data = updated_data
        self.save_data()