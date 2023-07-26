import tkinter as tk
# from Admin import Admin
from tkinter import ttk


class Admin:
    def __init__(self, username, password, address):
        self.users = {username: password, "user": "password123", "address": address}
    
    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False
        



class LoginWindow(tk.Tk):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.title("Login")
        self.geometry("300x150")
        self.resizable(False, False)
        
        # Create widgets
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack()
        
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()
        
        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()
        
        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.pack(pady=10)
        
        self.label_error = tk.Label(self, fg="red")
        self.label_error.pack()
    
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if self.admin.login(username, password):
            # Open the main window
            self.destroy()
            MainWindow(self.admin).mainloop()
        else:
            self.label_error.config(text="Incorrect username or password")



class MainWindow(tk.Tk):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.title("Main")
        self.geometry("500x500")
        self.resizable(False, False)
        
        # Create widgets and add functionality
        self.button_register_doctor = tk.Button(self, text="Register/View/Update/Delete Doctor", command=self.register_view_update_delete_doctor)
        self.button_register_doctor.pack(pady=10)
        
        self.button_discharge_patients = tk.Button(self, text="Discharge Patients", command=self.discharge_patients)
        self.button_discharge_patients.pack(pady=10)
        
        self.button_admit_patient = tk.Button(self, text="view discharged patients", command=self.view_discharged_patient)
        self.button_admit_patient.pack(pady=10)
        
        self.button_register_patient = tk.Button(self, text="Assign doctor to a Patient", command=self.assign_doctor_patient)
        self.button_register_patient.pack(pady=10)
        
        self.button_register_nurse = tk.Button(self, text="Relocate doctor to the patient", command=self.relcate_patient_doctor)
        self.button_register_nurse.pack(pady=10)
        
        self.button_view_reports = tk.Button(self, text="View management Reports", command=self.view_reports)
        self.button_view_reports.pack(pady=10)
        
        self.button_view_appointments = tk.Button(self, text="update admin details", command=self.update_admin_deatils)
        self.button_view_appointments.pack(pady=10)
        
        self.button_log_out = tk.Button(self, text="Quit", command=self.log_out)
        self.button_log_out.pack(pady=10)
        
    def register_view_update_delete_doctor(self):
        self.destroy() # Close the current window
        DoctorManagementWindow(self.admin).mainloop() # Open the doctor management window
        
    def discharge_patients(self):
        self.destroy() # Close the current window
        DischargePatientWindow(self.admin).mainloop() # Open the discharge patients window
        
    def view_discharged_patient(self):
        self.destroy() # Close the current window
        sorry(self.admin).mainloop() # Open the admit patient window
        
    def assign_doctor_patient(self):
        self.destroy() # Close the current window
        sorry(self.admin).mainloop() # Open the patient management window
        
    def relcate_patient_doctor(self):
        self.destroy() # Close the current window
        sorry(self.admin).mainloop() # Open the nurse management window
        
    def view_reports(self):
        self.destroy() # Close the current window
        sorry(self.admin).mainloop() # Open the reports window
        
    def update_admin_deatils(self):
        self.destroy() # Close the current window
        sorry(self.admin).mainloop() # Open the appointments window
        
    def log_out(self):
        self.destroy() # Close the current window
        LoginWindow().mainloop() # Open the login window

class sorry(tk.Tk):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.title("Main")
        self.geometry("500x500")


        self.label_id = tk.Label(self, text="Sorry System is Under development! Try again in few days:")
        self.label_id.pack()

       

        self.button_submit = tk.Button(self, text="back", command=self.sub)
        self.button_submit.pack(pady=10)

    def sub(self):
        self.destroy()
        MainWindow(self.admin).mainloop()





class DischargePatientWindow(tk.Tk):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.title("Main")
        self.geometry("500x500")

        # Create a Treeview widget
        tree = ttk.Treeview(columns=('First Name', 'Surname', 'Age', 'Mobile', 'Postcode'), show='headings')

        # Add columns to the Treeview widget
        tree.heading('First Name', text='First Name')
        tree.heading('Surname', text='Surname')
        tree.heading('Age', text='Age')
        tree.heading('Mobile', text='Mobile')
        tree.heading('Postcode', text='Postcode')

        # Add data to the Treeview widget
        patients = [('Sara','Smith', '20', '07012345678', 'B1 234'),
                    ('Mike', 'Jones', '37', '07555551234', 'L2 2AB'),
                    ('David', 'Smith', '15', '07123456789', 'C1 ABC')]
        for patient in patients:
            tree.insert('', 'end', values=patient)

        # Pack the Treeview widget into the window
        tree.pack()

        self.label_discharge = tk.Label(self, text="Do you want to discharge a patient:")
        self.label_discharge.pack()

        self.label_heading = tk.Label(self, text="-----Discharge Patient-----")
        self.label_heading.pack()

        self.label_id = tk.Label(self, text="Please enter the patient ID:")
        self.label_id.pack()

        self.entry_id = tk.Entry(self)
        self.entry_id.pack()

        self.button_submit = tk.Button(self, text="Discharge", command=self.submit)
        self.button_submit.pack(pady=10)

        self.label_error = tk.Label(self, fg="red")
        self.label_error.pack()

        self.button_submit = tk.Button(self, text="back", command=self.sub)
        self.button_submit.pack(pady=10)

    def sub(self):
        self.destroy()
        MainWindow(self.admin).mainloop()

    def submit(self):
        # patient_id = self.entry_id.get()
        # if self.admin.discharge_patient(patient_id):
        self.label_success = tk.Label(self, text="Patient was successfully discharged")
        self.label_success.pack()
        # else:
        #     self.label_error.config(text="Invalid patient ID")        



class DoctorManagementWindow(tk.Tk):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.title("Main")
        self.geometry("500x500")
        self.resizable(False, False)

        self.button_register_doctor = tk.Button(self, text="Register", command=self.Register)
        self.button_register_doctor.pack(pady=10)
        
        self.button_discharge_patients = tk.Button(self, text="view", command=self.View)
        self.button_discharge_patients.pack(pady=10)
        
        self.button_admit_patient = tk.Button(self, text="update", command=self.Update)
        self.button_admit_patient.pack(pady=10)
        
        self.button_register_patient = tk.Button(self, text="Delete", command=self.Delete)
        self.button_register_patient.pack(pady=10)

    def Register(self):
        self.destroy() # Close the current window
        Register(self.admin).mainloop() 

    def View(self):
        self.destroy() # Close the current window
        View(self.admin).mainloop()

    def Update(self):
        self.destroy() # Close the current window
        Update(self.admin).mainloop

    def Delete(self):
        self.destroy() # Close the current window
        Delete(self.admin).mainloop



class Delete(tk.Tk):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.title("Main")
        self.geometry("500x500")
        self.resizable(False, False)

        View(self.admin)

        self.label_username = tk.Label(self, text="Enter the id of doctor to delete:")
        self.label_username.pack()
        
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()
        
        # self.label_password = tk.Label(self, text="New_Surname:")
        # self.label_password.pack()
        
        # self.entry_password = tk.Entry(self, text="New_Surname")
        # self.entry_password.pack()

        # self.label_password = tk.Label(self, text="New_Speciality:")
        # self.label_password.pack()
        
        # self.entry_password = tk.Entry(self, text="New_Speciality")
        # self.entry_password.pack()
        
        self.button_login = tk.Button(self, text="submit", command=self.submit)
        self.button_login.pack(pady=10)
        
        self.label_error = tk.Label(self, fg="red")
        self.label_error.pack()
    
    def submit(self):
        
        # if self.admin.login(username, password):
            # Open the main window
        self.destroy()
        MainWindow(self.admin).mainloop()


class Update(tk.Tk):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.title("Main")
        self.geometry("500x500")
        self.resizable(False, False)

        self.label_username = tk.Label(self, text="New_Name:")
        self.label_username.pack()
        
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()
        
        self.label_password = tk.Label(self, text="New_Surname:")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(self, text="New_Surname")
        self.entry_password.pack()

        self.label_password = tk.Label(self, text="New_Speciality:")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(self, text="New_Speciality")
        self.entry_password.pack()
        
        self.button_login = tk.Button(self, text="submit", command=self.submit)
        self.button_login.pack(pady=10)
        
        self.label_error = tk.Label(self, fg="red")
        self.label_error.pack()
    
    def submit(self):
        
        # if self.admin.login(username, password):
            # Open the main window
        self.destroy()
        MainWindow(self.admin).mainloop()


class View(tk.Tk):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.title("Main")
        self.geometry("500x500")
        self.resizable(False, False)

       


        # Create a new tkinter window

        # Create a Treeview widget
        tree = ttk.Treeview(columns=('First Name', 'Surname', 'Specialty'), show='headings')

        # Add columns to the Treeview widget
        tree.heading('First Name', text='First Name')
        tree.heading('Surname', text='Surname')
        tree.heading('Specialty', text='Specialty')

        # Add data to the Treeview widget
        doctors = [('John', 'Doe', 'Cardiology'),
                ('Jane', 'Smith', 'Oncology'),
                ('Bob', 'Johnson', 'Pediatrics')]
        for doctor in doctors:
            tree.insert('', 'end', values=doctor)

        # Pack the Treeview widget into the window
        tree.pack()

        self.button_login = tk.Button(self, text="back", command=self.submit)
        self.button_login.pack(pady=10)
        
        self.label_error = tk.Label(self, fg="red")
        self.label_error.pack()
    
    def submit(self):
        
        # if self.admin.login(username, password):
            # Open the main window
        self.destroy()
        MainWindow(self.admin).mainloop()












class Register(tk.Tk):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.title("Main")
        self.geometry("500x500")
        self.resizable(False, False)

        self.label_username = tk.Label(self, text="Name:")
        self.label_username.pack()

        self.entry_username = tk.Entry(self)
        self.entry_username.pack()
        
        self.label_password = tk.Label(self, text="Surname:")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(self, text="Surname")
        self.entry_password.pack()

        self.label_password = tk.Label(self, text="Speciality:")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(self, text="Speciality")
        self.entry_password.pack()
        
        self.button_login = tk.Button(self, text="submit", command=self.submit)
        self.button_login.pack(pady=10)
        
        self.label_error = tk.Label(self, fg="red")
        self.label_error.pack()
    
    def submit(self):
        
        # if self.admin.login(username, password):
            # Open the main window
        self.destroy()
        MainWindow(self.admin).mainloop()
        

        



 


if __name__ == "__main__":
    admin = Admin("admin", "123", "123 Main Street")
    LoginWindow(admin).mainloop()


