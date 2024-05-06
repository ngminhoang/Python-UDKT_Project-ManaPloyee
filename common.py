from models import Employee


def cal_salary(staff: Employee):
    result = 0
    try:
        if staff.workingMonthCount >= 6:
            result = float(staff.revenue) * 4.5 / 100 + 3_500_000
        else:
            result = float(staff.revenue) * 3 / 100 + 2_000_000
    except Exception:
        pass
    return result

