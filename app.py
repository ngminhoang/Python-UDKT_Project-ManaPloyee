import tkinter as tk
from tkinter import ttk
from dataTable import DataTable

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ManaPloyees")

        # Load data from CSV using DataTable class (Replace 'data/data.csv' with your file path)
        self.data_table = DataTable('data/data.csv')
        self.data = self.data_table.get_data()

        # Calculate frame widths based on desired proportions
        left_frame_width = 1400*0.2
        right_frame_width = 1400*0.8

        # Create left frame (30% width)
        self.left_frame = tk.Frame(self.root, width=left_frame_width, height=400, bg='lightblue')
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create right frame (70% width)
        self.right_frame = tk.Frame(self.root, width=right_frame_width, height=400, bg='white')
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Display table in right frame
        self.display_table()

        # Create input fields in the left frame
        self.create_input_fields()



    def create_input_fields(self):

        # Labels and corresponding entry fields
        labels = ["ID", "Name", "Phone Number", "Email"]
        self.input_fields = {}
        for idx, label_text in enumerate(labels):
            label = tk.Label(self.left_frame, text=label_text + ":", anchor=tk.E, padx=5)
            label.grid(row=idx, column=0, sticky=tk.E)
            entry = tk.Entry(self.left_frame)
            entry.grid(row=idx, column=1, padx=5, pady=5, sticky=tk.W)
            self.input_fields[label_text] = entry

        # Role selection dropdown
        role_label = tk.Label(self.left_frame, text="Role:", anchor=tk.E, padx=5)
        role_label.grid(row=len(labels), column=0, sticky=tk.E)
        self.role_var = tk.StringVar(self.left_frame)
        self.role_var.set("Employee")  # Default role selection
        roles = ["Employee", "Manager"]
        role_menu = tk.OptionMenu(self.left_frame, self.role_var, *roles)
        role_menu.grid(row=len(labels), column=1, padx=5, pady=5, sticky=tk.W)

        # Button to add new record
        add_button = tk.Button(self.left_frame, text="Add Record", command=self.add_record)
        add_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

    def display_table(self):
        # Create treeview widget to display table
        self.tree = ttk.Treeview(self.right_frame, columns=("ID", "Name", "Phone Number", "Email", "Role"), show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Define column headers
        headers = ["ID", "Name", "Phone Number", "Email", "Role"]
        for header in headers:
            self.tree.heading(header, text=header, command=lambda h=header: self.sort_by_column(h))
            self.tree.column(header, anchor=tk.CENTER)

        # Insert data rows into treeview
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
        """
        Add a new record to the table based on input field values.
        """
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
        values = [id_value, name_value, phone_value, email_value, role_value]
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
