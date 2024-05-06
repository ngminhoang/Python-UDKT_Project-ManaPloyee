from common import cal_salary, cal_income
from models import Staff, Employee, Manager
from dataTable import DataTable


class ManageEmployee:
    __data = DataTable()

    def getData(self):
        return self.__data.get_data()

    def addNewStaff(self, staff):
        self.__data.add_row(staff)

    def editStaff(self, staffId: int, newStaff):
        self.__data.delete_record_by_id(staffId)
        self.__data.add_row(newStaff)

    def deleteStaff(self, staffId: int, isPermanent: bool):
        if (isPermanent):
            self.__data.delete_record_by_id(staffId)
        # else:
        # need to confirm with team

    def searchStaffById(self, staffId: int):
        return
        # todo

    def searchStaffByName(self, staffName: str):
        return
        # todo

    # 0 truyền gì -> tổng lương empl & mana
    # truyền 1 -> tổng lương empl
    # truyền 0 -> tổng lương mana
    # truyền id -> lương cho nhân viên nhất định
    def salary_employee(self, staff_id=None, group: str = ""):
        all_staff = self.__data.get_data()
        result = 0
        if staff_id is None:
            for staff in all_staff:
                if staff['Role'] != group:
                    result += cal_salary(staff)
        else:
            for staff in all_staff:
                if staff['Role'] == staff_id:
                    result += cal_salary(staff)
        return result

    def income(self, cal_type: str = "group"):
        all_staff = self.__data.get_data()
        result = 0
        if cal_type == "group":
            for manager in all_staff:
                if str(manager['Role']) == "1":
                    result += cal_income(manager)
        else:
            for manager in all_staff:
                if str(manager['Role']) == "0":
                    result += cal_income(manager)
        return result


