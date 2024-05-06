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
        
        role_menu = tk.OptionMenu(self.left_frame, self.role_var, *roles, command=self.on_role_change)
        role_menu.grid(row=len(labels), column=1, padx=5, pady=5, sticky=tk.W)
        
        add_button = tk.Button(self.left_frame, text="Add Record", command=self.add_record)
        add_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)
    
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
                "Manager" if record.get("Role", False) else "Employee"
            ]
            self.tree.insert("", tk.END, values=values)

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

        ren = self.input_fields["Revenue"].get()
        w_month = self.input_fields["Working Month"].get()
        total_ren = self.input_fields["Total Revenue"].get()
        manage_group = self.input_fields["Manage Group"].get()
        empl_count = self.input_fields["Employee Count"].get()

        if not id_value or not name_value:
            # TODO: Loi o day
            # tk.messagebox.showerror("Error", "ID and Name are required fields.")
            return

        if(role_value!="Manager"):
            values = [id_value, name_value, phone_value, email_value, role_value, ren, w_month]
            staff = create_employee_from_list(values)
        else:
            values = [id_value, name_value, phone_value, email_value, role_value, total_ren, manage_group, empl_count]
            staff = create_manager_from_list(values)
        self.data_table.add_row(staff)
        self.tree.insert("", tk.END, values=values)


def main():
    root = tk.Tk()

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
