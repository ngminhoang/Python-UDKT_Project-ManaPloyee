import tkinter as tk
from tkinter import ttk
from dataTable import DataTable
from models import *

class DataApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("ManaPloyees")

        
        self.data_table = DataTable()
        self.data = self.data_table.get_data()

        
        left_frame_width = 1400*0.2
        right_frame_width = 1400*0.8

        
        self.left_frame = tk.Frame(self.root, width=left_frame_width, height=400, bg='lightblue')
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        
        self.right_frame = tk.Frame(self.root, width=right_frame_width, height=400, bg='white')
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        
        self.display_table(1)

        
        self.create_input_fields()



    def create_input_fields(self):

    # Labels and corresponding entry fields
        labels = ["ID", "Name", "Phone Number", "Email"]

        # Button to show all records
        show_all_button = tk.Button(self.left_frame, text="Show All", command=lambda: self.show_table(0))
        show_all_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        # Button to show employees
        show_employees_button = tk.Button(self.left_frame, text="Show Employees", command=lambda: self.show_table(1))
        show_employees_button.grid(row=len(labels) + 2, column=0, columnspan=2, pady=10)

        # Button to show managers
        show_managers_button = tk.Button(self.left_frame, text="Show Managers", command=lambda: self.show_table(2))
        show_managers_button.grid(row=len(labels) + 3, column=0, columnspan=2, pady=10)

        # Button to add a new record
        add_button = tk.Button(self.left_frame, text="Add Record", command=self.add_record)
        add_button.grid(row=len(labels) + 4, column=0, columnspan=2, pady=10)


    def show_table(self, display_type):
        """
        Display table based on the specified display type:
        - display_type 0: Show all records
        - display_type 1: Show employees
        - display_type 2: Show managers
        """
        self.data = self.data_table.get_data()
        self.display_table(display_type)
    

    def display_table(self,type):
        try:
            self.clear_tree()
            self.tree.delete(*self.tree.get_children())
        except:
            x=1
        if type == 0:
            self.tree = ttk.Treeview(self.right_frame, columns=("ID", "Name", "Phone Number", "Email", "Role"), show="headings")
            self.tree.pack(fill=tk.BOTH, expand=True)
            headers = ["ID", "Name", "Phone Number", "Email", "Role"]

            for header in headers:
                self.tree.heading(header, text=header, command=lambda h=header: self.sort_by_column(h))
                self.tree.column(header, anchor=tk.CENTER)

            for record in self.data:
                values = [
                    record.get("ID", ""),
                    record.get("Name", ""),
                    record.get("Phone Number", ""),
                    record.get("Email", ""),
                    "Manager" if record.get("Role", False) else "Employee"
                ]
                self.tree.insert("", tk.END, values=values)
        
        elif type == 1:
            self.tree = ttk.Treeview(self.right_frame, columns=("ID", "Name", "Phone Number", "Email", "Revenue", "Working Month Count"), show="headings")
            self.tree.pack(fill=tk.BOTH, expand=True)
            headers = ["ID", "Name", "Phone Number", "Email", "Revenue", "Working Month Count"]
            
            for header in headers:
                self.tree.heading(header, text=header, command=lambda h=header: self.sort_by_column(h))
                self.tree.column(header, anchor=tk.CENTER)

            for record in self.data:
                if record.get("Role", "")!="1":
                    values = [
                        record.get("ID", ""),
                        record.get("Name", ""),
                        record.get("Phone Number", ""),
                        record.get("Email", ""),
                        record.get("Revenue", ""),
                        record.get("Working Month Count", "")
                    ]
                    self.tree.insert("", tk.END, values=values)

        elif type == 2:
            self.tree = ttk.Treeview(self.right_frame, columns=("ID", "Name", "Phone Number", "Email", "Manage Group", "Employee Count","Total Revenue"), show="headings")
            self.tree.pack(fill=tk.BOTH, expand=True)
            headers = ["ID", "Name", "Phone Number", "Email", "Manage Group", "Employee Count","Total Revenue"]
            
            for header in headers:
                self.tree.heading(header, text=header, command=lambda h=header: self.sort_by_column(h))
                self.tree.column(header, anchor=tk.CENTER)

            for record in self.data:
                if record.get("Role", "")=="1":
                    values = [
                        record.get("ID", ""),
                        record.get("Name", ""),
                        record.get("Phone Number", ""),
                        record.get("Email", ""),
                        record.get("Manage Group", ""),
                        record.get("Employee Count", ""),
                        record.get("Total Revenue", "")
                    ]
                    self.tree.insert("", tk.END, values=values)


    def clear_tree(self):
        """
        Clear all items from the treeview.
        """
        # self.root.delete()
        for item in self.tree.get_children():
            self.tree.delete(item)

    def show_All(self):
        
        self.data = self.data_table.get_data()
        self.display_table(0)

    def sort_by_column(self, header):
        """
        Sort treeview data by the specified column header.
        """
        # Get current treeview items
        items = list(self.tree.get_children(""))

        # Sort items based on column values
        items.sort(key=lambda item: self.tree.set(item, header))

        # Rearrange treeview items
        for index, item in enumerate(items):
            self.tree.move(item, "", index)
    
    def add_record(self):
        # Retrieve input field values
        id_value = self.input_fields["ID"].get()
        name_value = self.input_fields["Name"].get()
        phone_value = self.input_fields["Phone Number"].get()
        email_value = self.input_fields["Email"].get()
        role_value = self.role_var.get()

        # Validate input (e.g., ensure required fields are not empty)
        if not id_value or not name_value:
            tk.messagebox.showerror("Error", "ID and Name are required fields.")
            return

        # Insert new record into the table (Treeview widget)
        if(role_value==0):
            values = [id_value, name_value, phone_value, email_value, role_value,12,12]
        else:
            values = [id_value, name_value, phone_value, email_value, role_value,12,12]
        staff = create_employee_from_list(values)
        self.data_table.add_row( staff)
        self.tree.insert("", tk.END, values=values)



def main():
    root = tk.Tk()

    # Set window size and position
    window_width = 1400
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.title("CSV Data Viewer")

    app = DataApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
