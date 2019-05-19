import hashlib 
from hospital.user import User
from hospital.doctor import Doctor
from hospital.patient import Patient

class UserAlreadyExistsError(Exception):
    pass
class NotValidPassword(Exception):
    pass
class MainController:
    @classmethod
    def _hash_password(cls,password):
        result = hashlib.sha256(password.encode()) 
        return result.hexdigest()
        # password = sha256_crypt.encrypt("password")
        # password2 = sha256_crypt.encrypt("password")

        # print(password)
        # print(password2)

        # print(sha256_crypt.verify("password", password))
    @staticmethod
    def _if_passwords_match(password1,password2):
       return password1==password2
    @classmethod
    def _validate_password(cls,password):
        return any(char.isdigit() for char in password) and len(password) > 3
    @classmethod
    def sign_in(cls,username,password):
        if cls._validate_password(password)==False:
             raise NotValidPassword('The password should contain more than 3 characters and it should contain at least one digit')
        password=cls._hash_password(password)
        current_user=User.find(username,password)
        return current_user
    @classmethod
    def sign_up(cls,username,password,second_password,status,full_name):

        if cls._validate_password(password)==False or cls._validate_password(password)==False:
            raise NotValidPassword('The password should contain more than 3 characters and it should contain at least one digit')

        hashed_pass1 = cls._hash_password(password)
        hashed_pass2 = cls._hash_password(second_password)
        print(cls._if_passwords_match(hashed_pass1,hashed_pass2))

        if User.find(username,hashed_pass1):
            raise UserAlreadyExistsError
      
        return User.create_new_user(username,hashed_pass1,status=status,full_name=full_name)
    @classmethod
    def list_all_free_slots(cls):
        return User.list_all_free_slots()
    @classmethod
    def list_all_booked_slots(cls):
        return User.list_all_booked_slots()
    @classmethod
    def list_slots(cls,date_to_check):
        return User.list_slots(date_to_check)
    @classmethod
    def list_booked_slots(cls,date_to_check):
        return User.list_booked_slots(date_to_check)
    @classmethod
    def add_doctor(cls,title,id_user):
        Doctor.create_new_doctor(title,id_user)
    @classmethod
    def add_patient(cls,address,age,unique_id,id_user):
        Patient.create_new_patient(address,age,unique_id,id_user)
    @classmethod
    def add_slot(cls,current_user,start_hour,end_hour,appointment_date,status):
        Doctor.add_new_slot(current_user,start_hour,end_hour,appointment_date,status)
    @classmethod
    def make_appointment(cls,current_user,slot_id):
        Patient.make_new_appointment(current_user,slot_id)
    @classmethod
    def cancel_appointment(cls,slot_id):
        Patient.cancel_appointment(slot_id)
    @classmethod
    def change_status_to_done(cls,slot_id):
        Patient.change_status_to_done(slot_id)
    @classmethod
    def show_appointments_for_this_user(cls,current_user):
        return Patient.show_appointments_for_this_user(current_user)
    @classmethod
    def show_members(cls,current_user):
        if current_user_is_doctor:
            return cls.show_patients(current_user)#returns a list of patients 
            #[roza,mimi]
        else:
            return cls.show_doctors(current_user)
    @staticmethod        
    def show_patients(cls,current_user):
        return Doctor.show_patients()