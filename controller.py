from common import to_num, cal_salary
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
        #else:
            #need to confirm with team
        

    def searchStaffById(self, staffId: int):
        return
        #todo

    def searchStaffByName(self, staffName: str):
        return 
        #todo

    def salary_employee(self, id = None):
        all_staff = self.__data
        result = 0
        if id is None:
            for staff in all_staff:
                if staff.role == "0":
                    result += cal_salary(staff)
        else:
            for staff in all_staff:
                if staff.id == id:
                    result += cal_salary(staff)
        return result
