from hospital.database import Database
class DatabaseConnectionError(Exception):
    pass

class Patient:
    db=Database()

    def __init__(self,title,id_user):
        self.title=title
        self.id_user=id_user

    @classmethod
    def find(cls,username,password):#we make the connection to the databaselayer
        result=cls.db.find_user(username,password)
        if result:#if it is None or [] it wont proceed
            cls(username,password,result['status'])

    @classmethod
    def create_new_patient(cls,address,age,unique_id,current_user):
        try:
            cls.db.create_patient(address,age,unique_id,current_user)
        except DatabaseConnectionError:
            sys.exit(1)
    @classmethod
    def make_new_appointment(cls,current_user,slot_id):
        try:
            cls.db.make_appointment(current_user,slot_id)
        except DatabaseConnectionError:
            sys.exit(1)
    @classmethod
    def cancel_appointment(cls,slot_id):
        try:
            cls.db.cancel_appointment(slot_id)
        except DatabaseConnectionError:
            sys.exit(1)
    @classmethod
    def change_status_to_done(cls,slot_id):
        try:
            cls.db.change_status_to_done(slot_id)
        except DatabaseConnectionError:
            sys.exit(1)
    @classmethod
    def delete_reserved_slot(cls,slot_id):
        try:
            cls.db.delete_reserved_slot(slot_id)
        except DatabaseConnectionError:
            sys.exit(1)
    @classmethod
    def show_appointments_for_this_user(cls,current_user):
        try:
            slots=cls.db.show_appointments_for_this_user(current_user)
        except DatabaseConnectionError:
            sys.exit(1)
        return slots
    # @property
    # def status(self):
    #     return self._status
    

