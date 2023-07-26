# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient





def patient_file(file_container):
    file=open(file_container,"r")
    list=[]
    for i,lines in enumerate(file):
        if lines != "\n" or lines != "":
            data=lines.split(",")
            data=[line.strip() for line in data]
            list.append(data)


    try: # trying to create list of object and returning
        list_a = []
        for j in list:
            patient = Patient(j[0], j[1], int(j[2]), j[3], j[4])
            list_a.append(patient)

        return list_a

    except: # incase creation of object fails, throwing error and giving error context
        print("error in file")

    



def main():
    """
    The main function to be run when the program starts
    """

    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]


    patients=patient_file("patients.txt")

    patients=admin.same_family(patients)
    # patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []



    # Keep trying to login until the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # Print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Relocating doctor to a patient')
        print(' 6- view management report')
        print(' 7- Update admin details')
        print(' 8- Quit')

        # Get the option
        op = input('Option: ')

        if op == '1':
            admin.doctor_management(doctors) # 1- Register/view/update/delete doctor
            

        elif op == '2':
            print("-----Patients-----")
        
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            admin.view(patients) # 2- View or discharge patients
            #ToDo2
            

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    admin.discharge(patients,discharged_patients)#ToDo3
                    

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            admin.view_discharge(discharged_patients)#ToDo4
            

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op =="5":
            admin.relocate(patients,doctors)

        elif op=="6":
            admin.management_report(patients,doctors)

        elif op == '7':
             # 5- Update admin detais
            admin.update_details()

        elif op == '8':
            # 6 - Quit
            print("See you Again !!BYE!!")
            #ToDo5
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
