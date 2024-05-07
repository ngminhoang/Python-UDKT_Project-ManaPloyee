from common import cal_salary, cal_income, format_currency
from models import Staff, Employee, Manager
from dataTable import DataTable


class ManageEmployee:
    __data = DataTable()

    def getData(self):
        return self.__data.get_data()

    def addNewStaff(self, staff):
        self.__data.add_row(staff)

    def editStaff(self, staffId, newStaff):
        self.__data.delete_record_by_id(staffId)
        self.__data.add_row(newStaff)

    def deleteStaff(self, staffId: int, isPermanent: bool):
        if (isPermanent):
            self.__data.delete_record_by_id(staffId)
        # else:
        # need to confirm with team

    def searchStaffById(self, staffId: int):
        self.__data.search_row_by_id(staffId)
        #todo

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
                    print(cal_salary(staff))
                    result += cal_salary(staff)
        else:
            for staff in all_staff:
                if staff['Role'] == staff_id:
                    print(cal_salary(staff))
                    result += cal_salary(staff)
        return format_currency(int(result))

    def income(self, cal_type: str):
        all_staff = self.__data.get_data()
        result = 0
        get_all = False
        if cal_type == "-1":
            get_all = True
        for staff in all_staff:
            if str(staff['Role']) != cal_type or get_all:
                result += cal_income(staff)
        return format_currency(int(result))


