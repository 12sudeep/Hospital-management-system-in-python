from Person import Person


class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname,age, mobile, postcode):
        """
        Args:
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        super().__init__(first_name,surname)
        self.__age= age
        self.__mobile=mobile
        self.__postcode=postcode #1st
        self.__doctor = 'None'
        self.__appointments=[]
        self.__symptoms=[]


       
    def get_doctor(self) :
        return self.__doctor #3rd
        

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor
    
    
    def get_symptoms(self):
        return self.__symptoms
    
    def set_symptoms(self,ne_symptoms):
        self.__symptoms=ne_symptoms

    def print_symptoms(self):
        op=input("Enter the symptoms: ")
        """prints all the symptoms"""
        print(op)#todo4
        self.set_symptoms(op)

    def get_appointment(self):
        return self.__appointments
    
    def more_appointment(self,appoint):
        self.__appointments.append(appoint)
        

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
