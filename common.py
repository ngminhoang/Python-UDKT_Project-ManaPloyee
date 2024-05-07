from __future__ import annotations

from dataTable import DataTable
from models import Employee, Manager
import pandas as pd
import re


def cal_salary(staff: Manager | Employee):
    result = 0
    try:
        if isinstance(staff, Employee):
            if int(staff['Working Month Count']) >= 6:
                result = float(staff['Revenue']) * 4.5 / 100 + 3_500_000
            else:
                result = float(staff['Revenue']) * 3 / 100 + 2_000_000
        else:
            result = float(staff['Total Revenue']) / int(staff['Employee Count']) * 8_000_000 + int(
                staff['Employee Count']) * 250_000
    except Exception as e:
        print(str(e))
    return result


def cal_income(staff: Manager | Employee):
    result = 0
    try:
        if staff["Role"] == "1":
            result = float(staff['Total Revenue'])
        else:
            result = float(staff['Revenue'])
    except Exception:
        pass
    return result


def validate(role, user_id, phone, email, revenue, working_month_count, total_revenue, employee_count):
    error_list = {}
    if user_id in get_user_ids():
        error_list.update({"id": "This Id existed"})
    if role == "Manager>":
        if not total_revenue.isdigit():
            error_list.update({"totalRevenue": "totalRevenue not valid"})
        if not employee_count.isdigit():
            error_list.update({"employeeCount": "Employee Count Month Count not valid"})
    else:
        if not revenue.isdigit():
            error_list.update({"renevue": "Renevue not valid"})
        if not working_month_count.isdigit():
            error_list.update({"workingMonthCount": "Working Month Count not valid"})
    if not re.match(r'\b\d{10}\b', phone):
        error_list.update({"phone": "Phone number not valid"})
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        error_list.update({"email": "Email not valid"})
    return error_list


def get_user_ids():
    all_user = pd.read_csv("data/data.csv")
    user_ids = all_user["ID"]
    return user_ids.values


def get_user_by_id(user_id):
    all_user = DataTable()
    for user in all_user.get_data():
        if user["ID"] == user_id:
            return user
    return None


def format_currency(number):
    # Convert number to string and reverse it
    number_str = str(number)[::-1]

    # Split the number into groups of three digits
    groups = [number_str[i:i + 3] for i in range(0, len(number_str), 3)]

    # Join the groups with '.' separator and reverse the result
    formatted_number = '.'.join(groups)[::-1]

    return formatted_number
