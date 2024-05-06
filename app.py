import tkinter as tk
from tkinter import ttk
from dataTable import DataTable
from models import *
from controller import *

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ManaPloyees")

        
        self.controller = ManageEmployee()
        self.data = self.controller.getData()

        
        left_frame_width = 1400*0.2
        right_frame_width = 1400*0.8

        
        self.left_frame = tk.Frame(self.root, width=left_frame_width, height=400, bg='lightblue')
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        
        self.right_frame = tk.Frame(self.root, width=right_frame_width, height=400, bg='white')
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        
        self.display_table()

        
        self.create_input_fields()



    def create_input_fields(self):
        labels = ["ID", "Name", "Phone Number", "Email", "Revenue", "Working Month", "Total Revenue", "Manage Group", "Employee Count"]
        self.input_fields = {}
        
        for idx, label_text in enumerate(labels):
            label = tk.Label(self.left_frame, text=label_text + ":", anchor=tk.E, padx=5)
            label.grid(row=idx, column=0, sticky=tk.E)
            entry = tk.Entry(self.left_frame)
            entry.grid(row=idx, column=1, padx=5, pady=5, sticky=tk.W)
            self.input_fields[label_text] = entry
        
        for field in ["Total Revenue", "Manage Group", "Employee Count"]:
                self.input_fields[field].delete(0, tk.END)
                self.input_fields[field].insert(0, "NOT USED") 
                self.input_fields[field].config(state=tk.DISABLED)

        role_label = tk.Label(self.left_frame, text="Role:", anchor=tk.E, padx=5)
        role_label.grid(row=len(labels), column=0, sticky=tk.E)
        
        self.role_var = tk.StringVar(self.left_frame)
        self.role_var.set("Employee")
        roles = ["Employee", "Manager"]

        self.add_button = tk.Button(self.left_frame, text="Add Record", command=self.add_record)
        self.add_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)
        
        role_menu = tk.OptionMenu(self.left_frame, self.role_var, *roles, command=self.on_role_change)
        role_menu.grid(row=len(labels), column=1, padx=5, pady=5, sticky=tk.W)
        
        self.update_button = tk.Button(self.left_frame, text="Update Record", command=self.update_record, state=tk.DISABLED)
        self.update_button.grid(row=len(labels) + 2, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self.left_frame, text="Delete Record", command=self.delete_record, state=tk.DISABLED)
        self.delete_button.grid(row=len(labels) + 3, column=0, columnspan=2, pady=10)

        self.lock_button = tk.Button(self.left_frame, text="Lock Record", command=self.lock_record, state=tk.DISABLED)
        self.lock_button.grid(row=len(labels) + 4, column=0, columnspan=2, pady=10)

        self.reset_button = tk.Button(self.left_frame, text="Reset", command=self.reset_record)
        self.reset_button.grid(row=len(labels) + 7, column=0, columnspan=2, pady=10)
    
    def update_record(self):
        id_value = self.input_fields["ID"].get()
        id_value = self.input_fields["ID"].get()
        name_value = self.input_fields["Name"].get()
        phone_value = self.input_fields["Phone Number"].get()
        email_value = self.input_fields["Email"].get()
        role_value = self.role_var.get()
        revenue_value = self.input_fields["Revenue"].get()
        working_month_value = self.input_fields["Working Month"].get()
        total_revenue_value = self.input_fields["Total Revenue"].get()
        manage_group_value = self.input_fields["Manage Group"].get()
        employee_count_value = self.input_fields["Employee Count"].get()

        if not id_value or not name_value:
            tk.messagebox.showerror("Error", "ID and Name are required fields.")
            return

        if(role_value=='Manager'):
            values = [id_value, name_value, phone_value, email_value, "Manager",total_revenue_value,manage_group_value,employee_count_value]
            staff = create_manager_from_list(values)
        else:
            values = [id_value, name_value, phone_value, email_value, "Employee",revenue_value,working_month_value]
            staff = create_employee_from_list(values)

        self.controller.editStaff(id_value,staff)



    def delete_record(self):
        print()

    def lock_record(self):
        print()

    def reset_record(self):
        self.enable_button_read()
        self.role_var.set("Employee")

        for field in["ID", "Name", "Phone Number", "Email", "Revenue", "Working Month", "Total Revenue", "Manage Group", "Employee Count"]:
                self.input_fields[field].config(state=tk.NORMAL)
                self.input_fields[field].delete(0, tk.END)      
                self.input_fields[field].insert(0, "")

        for field in ["Revenue", "Working Month"]:
                self.input_fields[field].config(state=tk.NORMAL)
                self.input_fields[field].delete(0, tk.END)      
                self.input_fields[field].insert(0, "")          
                                                                
        for field in ["Total Revenue", "Manage Group", "Employee Count"]:
                self.input_fields[field].delete(0, tk.END)          
                self.input_fields[field].insert(0, "NOT USED")      
                self.input_fields[field].config(state=tk.DISABLED)  
            
    def enable_button_writing(self):                
        self.add_button.config(state=tk.DISABLED)   
        self.update_button.config(state=tk.NORMAL)  
        self.delete_button.config(state=tk.NORMAL)  
        self.lock_button.config(state=tk.NORMAL)    

    def enable_button_read(self):
        self.add_button.config(state=tk.NORMAL)
        self.update_button.config(state=tk.DISABLED)
        self.delete_button.config(state=tk.DISABLED)
        self.lock_button.config(state=tk.DISABLED)

    def on_role_change(self, *args):
        selected_role = self.role_var.get()

        if selected_role == "Employee":
            for field in ["Revenue", "Working Month"]:
                self.input_fields[field].config(state=tk.NORMAL)
                self.input_fields[field].delete(0, tk.END)
                self.input_fields[field].insert(0, "") 

            for field in ["Total Revenue", "Manage Group", "Employee Count"]:
                self.input_fields[field].delete(0, tk.END)
                self.input_fields[field].insert(0, "NOT USED") 
                self.input_fields[field].config(state=tk.DISABLED)

        elif selected_role == "Manager":
            for field in ["Total Revenue", "Manage Group", "Employee Count"]:
                self.input_fields[field].config(state=tk.NORMAL)
                self.input_fields[field].delete(0, tk.END)
                self.input_fields[field].insert(0, "") 

            for field in ["Revenue", "Working Month"]:
                self.input_fields[field].delete(0, tk.END)
                self.input_fields[field].insert(0, "NOT USED")
                self.input_fields[field].config(state=tk.DISABLED)

    def display_table(self):
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
                "Manager" if record.get("Role","")=="1" else "Employee"
            ]
            self.tree.insert("", tk.END, values=values)
        self.tree.bind("<ButtonRelease-1>", self.on_row_click)

    def clear_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def reload_tree_data(self):
        self.data = self.controller.getData()
        for record in self.data:
            values = [
                record.get("ID", ""),
                record.get("Name", ""),
                record.get("Phone Number", ""),
                record.get("Email", ""),
                "Manager" if record.get("Role", "") == "1" else "Employee"
            ]
            self.tree.insert("", tk.END, values=values)

    def on_row_click(self, event):
        self.enable_button_writing()
        item = self.tree.selection()[0]
        values = self.tree.item(item, "values")
        print("Selected values:", values[4])
        self.input_fields["ID"].delete(0, tk.END)
        self.input_fields["ID"].insert(0, values[0])
        self.input_fields["Name"].delete(0, tk.END)
        self.input_fields["Name"].insert(0, values[1])
        self.input_fields["Phone Number"].delete(0, tk.END)
        self.input_fields["Phone Number"].insert(0, values[2])
        self.input_fields["Email"].delete(0, tk.END)
        self.input_fields["Email"].insert(0, values[3])
        if values[4]=="Employee":
            self.role_var.set("Employee")
            for row in self.data:
                if row["ID"] == values[0] and row["Role"] == "0" :
                    print(row)
                    self.input_fields["Revenue"].config(state=tk.NORMAL)
                    self.input_fields["Revenue"].delete(0, tk.END)
                    self.input_fields["Revenue"].insert(0, row["Revenue"])
                    self.input_fields["Working Month"].config(state=tk.NORMAL)
                    self.input_fields["Working Month"].delete(0, tk.END)
                    self.input_fields["Working Month"].insert(0, row["Working Month Count"])

            for field in ["Total Revenue", "Manage Group", "Employee Count"]:
                self.input_fields[field].delete(0, tk.END)
                self.input_fields[field].insert(0, "NOT USED") 
                self.input_fields[field].config(state=tk.DISABLED)      

        if values[4]=="Manager":
            self.role_var.set("Manager")
            for row in self.data:
                if row["ID"] == values[0] and row["Role"] == "1" :
                    print(row)
                    self.input_fields["Total Revenue"].config(state=tk.NORMAL)
                    self.input_fields["Total Revenue"].delete(0, tk.END)
                    self.input_fields["Total Revenue"].insert(0, row["Total Revenue"])
                    self.input_fields["Manage Group"].config(state=tk.NORMAL)
                    self.input_fields["Manage Group"].delete(0, tk.END)
                    self.input_fields["Manage Group"].insert(0, row["Manage Group"])
                    self.input_fields["Employee Count"].config(state=tk.NORMAL)
                    self.input_fields["Employee Count"].delete(0, tk.END)
                    self.input_fields["Employee Count"].insert(0, row["Employee Count"])

            for field in ["Revenue", "Working Month"]:
                self.input_fields[field].delete(0, tk.END)
                self.input_fields[field].insert(0, "NOT USED")
                self.input_fields[field].config(state=tk.DISABLED)         
            
        # if(values[4]==)

    def sort_by_column(self, header):
        items = list(self.tree.get_children(""))

        items.sort(key=lambda item: self.tree.set(item, header))

        for index, item in enumerate(items):
            self.tree.move(item, "", index)
    
    def add_record(self):
        id_value = self.input_fields["ID"].get()
        name_value = self.input_fields["Name"].get()
        phone_value = self.input_fields["Phone Number"].get()
        email_value = self.input_fields["Email"].get()
        role_value = self.role_var.get()
        revenue_value = self.input_fields["Revenue"].get()
        working_month_value = self.input_fields["Working Month"].get()
        total_revenue_value = self.input_fields["Total Revenue"].get()
        manage_group_value = self.input_fields["Manage Group"].get()
        employee_count_value = self.input_fields["Employee Count"].get()

        if not id_value or not name_value:
            tk.messagebox.showerror("Error", "ID and Name are required fields.")
            return

        if(role_value=='Manager'):
            values = [id_value, name_value, phone_value, email_value, "Manager",total_revenue_value,manage_group_value,employee_count_value]
            staff = create_manager_from_list(values)
        else:
            values = [id_value, name_value, phone_value, email_value, "Employee",revenue_value,working_month_value]
            staff = create_employee_from_list(values)
            
        print(role_value)
        self.controller.addNewStaff( staff)
        self.tree.insert("", tk.END, values=values)



def main():
    root = tk.Tk()

    window_width = 1400
    window_height = 600
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
