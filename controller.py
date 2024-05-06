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
        #else:
            #need to confirm with team
        

    def searchStaffById(self, staffId: int):
        return
        #todo

    def searchStaffByName(self, staffName: str):
        return 
        #todo