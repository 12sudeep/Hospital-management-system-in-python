from Doctor import Doctor
from Patient import Patient




class Admin():
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ""):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

     





    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones

        return self.__username in username and self.__password == password  #ToDo1
    

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name=input("Enter the first name of the doctor: ")  #ToDo2
        surname=input("Enter the surname of the doctor: ")
        speciality=input("Enter the speciality of the doctor: ")
        
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input("Input: ")  #ToDo3


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name,surname,speciality = self.get_doctor_details() #ToDo4

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists=True
                    break  #ToDo5
                    # save time and end the loop
            
            if name_exists==False:
                if first_name.strip()=="" or  surname.strip()=="" or speciality.strip()=="":
                    print("Doctor's details cannot be empty. please try again!")
                else:
                    new_doctor=Doctor(first_name,surname,speciality)
                    doctors.append(new_doctor) #ToDo6
                # add the doctor ...
                                                            # ... to the list of doctors
                    print('The Doctor is sucessfully registered.')
                    return doctors

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            print("ID |          Full name           |  Speciality")
            self.view(doctors) #ToDo7


        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        break
                        
                    else:
                        print("Id of the doctor is not found")

                        
                            # doctor_index is the ID mines one (-1)
                            

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

                # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            try:
                op = int(input('Input: ')) # make the user input lowercase
                if op==1:
                    new_name=input("Enter the new first name: ")
                    if new_name.strip()=="":
                        print("Doctor's details cannot be empty. please try again!")
                    else:
                        new_name=new_name.title()
                        doctors[index].set_first_name(new_name)
                        print("doctor details updated")
                if op==2:
                    new_surname=input("Enter the new surname: ")
                    if new_surname.strip()=="":
                        print("Doctor's details cannot be empty. please try again!")
                    else:
                        new_surname=new_surname.title()
                        doctors[index].set_surname(new_surname)
                        print("doctor details updated")

                if op==3:
                    new_speciality=input("Enter the new speciality: ")
                    if new_speciality.strip()=="":
                        print("Doctor's details cannot be empty. please try again!")
                    else:

                        new_speciality=new_speciality.lower()
                        doctors[index].set_speciality(new_speciality)
                        print("doctor details updated")

            except:
                print("Error occured due to wrong input please try again")
            

            #ToDo8
            

        # Delete
        elif op == '4':
        
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

                
        
            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: '))-1
                index=self.find_index(doctor_index,doctors)
                if index!=False:
                    doctors.pop(doctor_index)
                    print("Id of doctor sucessfully deleted")
                    return doctors                            
                
                else:
                    print("The entered id was not found")

            except:
                print("Error occured due to wrong input. please try again")

                            # doctor_index is the ID mines one (-1)
                            
                    #ToDo9

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
        #ToDo10



    def same_family(self,patient):
    
        dict = {}
        for i in patient:
            last_name = i.get_surname()
            if last_name not in dict:
                dict[last_name] = [i]
            else:
                patient_list = dict[last_name]
                patient_list.append(i)
                dict[last_name] = patient_list
    
        grouped_patients = []
        for j, patient_data in dict.items():
            grouped_patients.extend(patient_data)
        
        return grouped_patients
    


    def relocate(self,patients,doctors):
        patients = [i for i in patients if i.get_doctor() != 'None']

        if len(patients) == 0:
            print("No patient assigned to any doctors. Assign a doctor to a patient.")
            return
        else:
            print("---Relocate a patient from one doctor to another---")

            print("-----Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            self.view(patients)

            index = input('Please enter the patient ID: ')
            patient_index = index

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        

        try:
            doctor_index = int(input('Please enter the doctor ID: '))
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                #ToDo11
                
                print('The patient is now relocated to a new doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')



    def assign_doctor_to_patient(self, patients, doctors):
        while True:
            """
            Allow the admin to assign a doctor to a patient
            Args:
                patients (list<Patients>): the list of all the active patients
                doctors (list<Doctor>): the list of all the doctors
            """
            print("-----Assign-----")

            print("-----Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            self.view(patients)

    

            try:
                patient_index = input('Please enter the patient ID: ')
                # patient_index is the patient ID mines one (-1)
            
                patient_index = int(patient_index) -1
        

                # check if the id is not in the list of patients
                if patient_index not in range(len(patients)):
                    print('The id entered was not found.')
                    return # stop the procedures

            except ValueError: # the entered id could not be changed into an int
                print('The id entered is incorrect')
                return # stop the procedures

            print("-----Doctors Select-----")
            print('Select the doctor that fits these symptoms:')
            patients[patient_index].print_symptoms() # print the patient symptoms

            print('--------------------------------------------------')
            print('ID |          Full Name           |  Speciality   ')
            self.view(doctors)
            

            try:
                doctor_index = int(input('Please enter the doctor ID: '))
                # doctor_index is the patient ID mines one (-1)
                doctor_index = int(doctor_index) -1

                # check if the id is in the list of doctors
                if self.find_index(doctor_index,doctors)!=False:
                        
                    # link the patients to the doctor and vice versa
                    patients[patient_index].link(doctors[doctor_index].full_name())
                    doctors[doctor_index].add_patient(patients[patient_index].full_name())
                    #ToDo11
                    
                    print('The patient is now assign to the doctor.')

                # if the id is not in the list of doctors
                else:
                    print('The id entered was not found.')

            

            except ValueError: # the entered id could not be changed into an in
                print('The id entered is incorrect')
        


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
 
        print("-----Discharge Patient-----")

        try:
            patient_index = int(input('Please enter the patient ID: '))-1

            if patient_index in range(len(patients)):
                discharge_patients.append(patients.pop(patient_index))
                
                print("Patient was sucessfully discharged")

            

                # open the file for reading
                with open("patients.txt", "r") as f:
                    lines = f.readlines()

                # remove the second line (index 1)
                del lines[patient_index]

                # open the file for writing
                with open("patients.txt", "w") as f:
                    # write the remaining lines to the file
                    for line in lines:
                        f.write(line)



                # self.change("patients.txt",patients[patient_index])
                # self.view_discharge(discharge_patients)
                self.view_patient(patients)
            else:
                print("patient id wasnot found")
        except:
            print("Error occured due to wrong input please try again")


    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        if len(discharged_patients) == 0:
            print("No patient is currently discharged.Thankyou! ")
            return
        else:

            print("-----Discharged Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            self.view(discharged_patients)        #ToDo13
    


    def management_report(self,patients,doctors):
        # Initialize the variables
        num_doctors = len(doctors)
        num_patients = len(patients)
        patients_per_doctor = {}
        appts_per_doctor = {}
        illness_counts = {}

        # Calculate the statistics
        for doctor in doctors:
            doctor_name = doctor.full_name()
            patients_per_doctor[doctor_name] = 0
            appts_per_doctor[doctor_name] = 0
            for patient in patients:
                if patient.get_doctor() == doctor_name:
                    patients_per_doctor[doctor_name] += 1
                    appts_per_doctor[doctor_name] += len(patient.get_appointment())

        for patient in patients:
            for symptom in patient.get_symptoms():
                if symptom not in illness_counts:
                    illness_counts[symptom] = 1
                else:
                    illness_counts[symptom] += 1

        # Print the report
        print("\n---Management Report---\n")
        print(f"{'Total number of doctors':<50} : {num_doctors}")
        print(f"{'Total number of patients':<50} : {num_patients}")
        for doctor_name, num_patients in patients_per_doctor.items():
            print(f"{'Total number of patients per doctor':<50} : {doctor_name:<15} : {num_patients:>3} patients")
        for doctor_name, num_appts in appts_per_doctor.items():
            print(f"{'Total number of appointments per month per doctor':<50} : {doctor_name:<15} : {num_appts:>3} appointments")
        for symptom, num_patients in illness_counts.items():
            print(f"{'Total number of patients based on the illness':<50} : {symptom:<15} : {num_patients:>3} patients\n")




    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        try:
            op = int(input('Input: '))

            if op == 1:
                n_username=input("Enter new username: ")
                self.__username = n_username        #ToDo14
                print("details updated")


            elif op == 2:
                password = input('Enter the new password: ')
                # validate the password
                if password == input('Enter the new password again: '):
                    self.__password = password
                    print("details updated")

            elif op == 3:
                n_address=input("Enter new address: ")      #ToDo15
                self.__address=n_address
                print("details updated")

            else:
                print("Invalid input")#ToDo16
        except:
            print("Error occured due to wrong input")

