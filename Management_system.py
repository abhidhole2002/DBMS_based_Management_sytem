from tkinter import *
from tkinter import ttk, messagebox,simpledialog,filedialog
import pymysql
from fpdf import FPDF

# Create a connection to MySQL
con = pymysql.connect(
    host="host",
    user="user",
    password="password",
    database="database")
cur = con.cursor()

# Create the table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS std (
        roll_no VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50),
        gender VARCHAR(10),
        contact VARCHAR(15),
        dob VARCHAR(20),
        address TEXT
    )
""")
con.commit()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1520x780+0+0")
        
        self.username = StringVar()
        self.password = StringVar()

        heading = Frame(self.root, bd=3, relief=RIDGE, bg="gold")
        heading.place(x=100, y=40, width=1300, height=80)
        
        lbl_heading = Label(heading, text="WELCOME TO MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"),bg="gold")
        lbl_heading.pack(pady=20)

        login = Frame(self.root, bd=3, relief=RIDGE, bg="navajo white")
        login.place(x=450, y=180, width=600, height=300)

    
        
        lbl_username = Label(login, text="Username:", font=("times new roman", 20, "bold"),bg="navajo white")
        lbl_username.pack(pady=10)
        entry_username = Entry(login, textvariable=self.username, font=("times new roman", 14),bd=5,relief=GROOVE)
        entry_username.pack(pady=10)

        lbl_password = Label(login, text="Password:", font=("times new roman", 20, "bold"),bg="navajo white")
        lbl_password.pack(pady=10)
        entry_password = Entry(login, textvariable=self.password, show="*", font=("times new roman", 14),bd=5,relief=GROOVE)
        entry_password.pack(pady=10)

        btn_login = Button(login, text="Login", width=10, command=self.login, font=("times new roman", 14, "bold"), bg="#4CAF50", fg="white", bd=4)
        btn_login.pack(pady=10)

    def login(self):
        # Validate the credentials (You should implement a proper validation logic here)
        if self.username.get() == "123" and self.password.get() == "123":
            self.root.destroy()  # Close the login window
            self.open_main_window()
        else:
            messagebox.showerror("Unauthorized", "You are an unauthorized person!")

    def open_main_window(self):
        root = Tk()
        obj = Student(root)
        root.mainloop()


class Student():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1520x780+0+0")

        title = Label(self.root, text="Student Management System", bd=4,relief=GROOVE, font=("times new roman", 40, "bold"), bg="firebrick1", fg="black")
        title.pack(side=TOP, fill=X)

        # All Variables
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
    
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # Manage Frame
        Manage_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="LightSteelBlue1")
        Manage_Frame.place(x=20, y=100, width=450, height=630)

        m_title = Label(Manage_Frame, text="Manage Student", bg="LightSteelBlue1", fg="black",
                        font=("times new roman", 40, "bold"))
        m_title.grid(row=0, columnspan=4, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No:", bg="LightSteelBlue1", fg="black",font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        
        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name:", bg="LightSteelBlue1", fg="black",font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        
        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email:", bg="LightSteelBlue1", fg="black",font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        
        txt_Email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender:", bg="LightSteelBlue1", fg="black",font=("times new roman", 22, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var,font=("times new roman", 13, "bold"), state='readonly')
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_Contact = Label(Manage_Frame, text="Contact:", bg="LightSteelBlue1", fg="black",font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        
        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_Dob = Label(Manage_Frame, text="D.O.B:", bg="LightSteelBlue1", fg="black",font=("times new roman", 20, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        
        txt_Dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address:", bg="LightSteelBlue1", fg="black",font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        
        self.txt_Address = Text(Manage_Frame, width=30, height=3, font=("times new roman", 10, "bold"))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # Button Frame
        btn_Frame = Frame(Manage_Frame, bd=1, relief=GROOVE, bg="azure")
        btn_Frame.place(x=15, y=525, width=380)

        Addbtn = Button(btn_Frame, text="Submit", width=8, bg="#7FFFD4", command=self.add_students, pady=6,font=("times new roman", 15, "bold"))
        Addbtn.grid(row=0, column=0, padx=10, pady=10)
        
        updatebtn = Button(btn_Frame, text="Update", width=8, bg="#7FFFD4", command=self.update_data, pady=6,font=("times new roman", 15, "bold"))
        updatebtn.grid(row=0, column=1, padx=10, pady=10)
        
        Clearbtn = Button(btn_Frame, text="Clear", width=8, bg="#7FFFD4", command=self.clear, pady=6,font=("times new roman", 15, "bold"))
        Clearbtn.grid(row=0, column=2, padx=10, pady=10)
        
        # 2nd Details Frame
        Detials_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="LightSteelBlue1")
        Detials_Frame.place(x=500, y=100, width=1000, height=630)
        
        truncate = Frame(Detials_Frame, bd=3, relief=RIDGE, bg="LightSteelBlue1")
        truncate.place(x=850, y=575, width=117, height=41)

        lbl_search = Label(Detials_Frame, text="Search By", bg="LightSteelBlue1", fg="black",font=("times new roman", 18, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detials_Frame, textvariable=self.search_by, width=10,font=("times new roman", 16, "bold"), state='readonly')
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detials_Frame, textvariable=self.search_txt, width=20, font=("times new roman", 13, "bold"),bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detials_Frame, text="Search", bg="#7FFFD4", width=8, pady=1, command=self.search_data,font=("times new roman", 13, "bold"))
        searchbtn.grid(row=0, column=3, padx=10, pady=10)
        
        showallbtn = Button(Detials_Frame, text="Show All", bg="#7FFFD4", width=8, pady=1, command=self.fetch_data,font=("times new roman", 13, "bold"))
        showallbtn.grid(row=0, column=4, padx=10, pady=10)
        
        deletebtn = Button(Detials_Frame, text="Delete", width=8, bg="#7FFFD4", command=self.delete_data, pady=1,font=("times new roman", 13, "bold"))
        deletebtn.grid(row=0, column=5, padx=10, pady=10)
        
        print_btn = Button(Detials_Frame, text="Print", width=8, bg="#7FFFD4", command=self.generate_pdf, pady=1,font=("times new roman", 13, "bold"))
        print_btn.grid(row=0, column=6, padx=10, pady=10)
    
        Delete_DB_btn = Button(truncate, text="TRUNCATE", width=10, bg="red", command=self.truncate_database, pady=1, font=("times new roman", 13, "bold"))
        Delete_DB_btn.grid( padx=1, pady=1)

        # Table Frame
        Table_Frame = Frame(Detials_Frame, bd=2, relief=RIDGE, bg="LightSteelBlue3")
        Table_Frame.place(x=10, y=70, width=960, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, column=("roll", "name", "email", "gender", "contact", "dob", "Address"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.Student_table.xview)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("times new roman", 12, "bold"), bg="gray")

        self.Student_table.heading("roll", text="Roll NO.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")

        style.configure("Treeview", font=("times new roman", 10))

        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_students(self):
        
        if self.Roll_No_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            # Check if Roll No already exists
            cur.execute("SELECT * FROM std WHERE roll_no=%s", self.Roll_No_var.get())
            existing_record = cur.fetchone()
            if existing_record:
                messagebox.showerror("Error", "Record with Roll No already exists!")
            else:
                cur.execute("INSERT INTO std VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (self.Roll_No_var.get(),
                         self.name_var.get(),
                         self.email_var.get(),
                         self.gender_var.get(),
                         self.contact_var.get(),
                         self.dob_var.get(),
                         self.txt_Address.get('1.0', END)))
            con.commit()
            self.fetch_data()
            self.clear()
        messagebox.showinfo("Success", "Record has been inserted")


    def fetch_data(self):
        cur.execute("SELECT * FROM std")
        rows = cur.fetchall()
        self.Student_table.delete(*self.Student_table.get_children())  # Clear the table
        if len(rows) != 0:
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        else:
            messagebox.showinfo("Information", "No data available")

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])

    def update_data(self):
        cur.execute("UPDATE std SET name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s WHERE roll_no=%s",
                    (self.name_var.get(),
                     self.email_var.get(),
                     self.gender_var.get(),
                     self.contact_var.get(),
                     self.dob_var.get(),
                     self.txt_Address.get('1.0', END),
                     self.Roll_No_var.get()))

        con.commit()
        self.fetch_data()
        self.clear()

    def delete_data(self):
        selected_item = self.Student_table.focus()
        if not selected_item:
            messagebox.showerror("Error", "No record selected")
            return

        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this record?")
        if confirmation:
            row_values = self.Student_table.item(selected_item)["values"]
            roll_no = row_values[0]
            cur.execute("DELETE FROM std WHERE roll_no=%s", roll_no)
            con.commit()
            self.fetch_data()  # Fetch data again after deletion
            self.clear()


    def search_data(self):
        cur.execute("select * from std where " + str(self.search_by.get())+" Like '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        else:
            messagebox.showinfo("Information", "No data available")


    def truncate_database(self):
    # Add your desired password here
        correct_password = "YourPassword123"

    # Prompt the user for the password
        user_password = simpledialog.askstring("Password", "Enter the password to delete the database:", show='*')

    # Check if the entered password is correct
        if user_password == correct_password:
        # Execute SQL queries to delete all records from the table
            cur.execute("DELETE FROM std")
            con.commit()

        # Check if any rows were affected
            if cur.rowcount > 0:
                messagebox.showinfo("Success", "Database truncated successfully!")
                self.fetch_data(self)
            else:
                messagebox.showinfo("Information", "The database is already empty.")
        else:
            messagebox.showerror("Unauthorized", "You are an unauthorized person!")



    def generate_pdf(self):
    # Get the registration ID from the input field
        reg_id = self.Roll_No_var.get()

    # Check if the ID is provided
        if not reg_id:
            messagebox.showerror("Error", "Please enter a valid Registration ID!")
            return

    # Retrieve registration details from the database
        cur.execute("SELECT * FROM std WHERE roll_no=%s", reg_id)
        registration = cur.fetchone()

    # Check if registration exists
        if not registration:
            messagebox.showerror("Error", "Registration not found!")
            return

    # Create a PDF document
        pdf = FPDF()
        pdf.add_page()

    # Set font properties
        pdf.set_font("Arial", size=12)
        pdf.set_font("Arial", "B", size=24)

    # Add form data to the PDF
        pdf.cell(0, 10, "", ln=True)
        pdf.cell(0, 10, "", ln=True)
        pdf.cell(0, 10, " Registration Receipt", ln=True, align="C")

        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "", ln=True)
        pdf.cell(0, 10, f"                                    Roll No :           {registration[0]}", ln=True)
        pdf.cell(0, 10, f"                                    Full Name :         {registration[1]}", ln=True)
        pdf.cell(0, 10, f"                                    Email ID :          {registration[2]}", ln=True)
        pdf.cell(0, 10, f"                                    Gender :            {registration[3]}", ln=True)
        pdf.cell(0, 10, f"                                    Contact :           {registration[4]}", ln=True)
        pdf.cell(0, 10, f"                                    Date of Birth :     {registration[5]}", ln=True)
        pdf.cell(0, 10, f"                                    Address :           {registration[6]}", ln=True)

    # Prompt the user to select a file path for saving the PDF
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf")

    # Save the PDF if a file path is selected
        if file_path:
            pdf.output(file_path)
            messagebox.showinfo("Success", "PDF generated and saved successfully!")
        else:
            messagebox.showinfo("Info", "PDF generation cancelled.")


if __name__ == "__main__":
    root = Tk()
    login = LoginWindow(root)
    root.mainloop()
