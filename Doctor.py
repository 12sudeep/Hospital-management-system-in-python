from Person import Person 



class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname,speciality):
        """
        Args:
            speciality (string): Doctor`s speciality
        """
        super().__init__(first_name,surname)
        self.__speciality = speciality
        self.__patient = []
        self.__appointments = []


    def get_speciality(self) :
        return self.__speciality #6th

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality #7th

    def get_patient(self):
        return self.__patient
    
    def add_patient(self, patient):
        self.__patient.append(patient)
    
    def get_appointment(self):
        return self.__appointments
    
    def add_appointment(self, appointment):
        self.__appointments.append(appointment)


    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'


