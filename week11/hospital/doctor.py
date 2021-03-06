from hospital.database import Database
class DatabaseConnectionError(Exception):
    pass

class Doctor:
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
    def create_new_doctor(cls,title,current_user):
        try:
            cls.db.create_doctor(title,current_user)
        except DatabaseConnectionError:
            sys.exit(1)

    @classmethod
    def add_new_slot(cls,current_user,start_hour,end_hour,appointment_date,status):
        try:
            cls.db.add_slot(current_user,start_hour,end_hour,appointment_date,status)
        except DatabaseConnectionError:
            sys.exit(1)
    @classmethod
    def update_slot(cls,slot_id,start_hour,end_hour):
        try:
            cls.db.update_slot(slot_id,start_hour,end_hour)
        except DatabaseConnectionError:
            sys.exit(1)
    @classmethod
    def delete_slot(cls,slot_id):
        try:
            cls.db.delete_slot(slot_id)
        except DatabaseConnectionError:
            sys.exit(1)
    @classmethod
    def show_appointments_with_this_doctor(cls,current_user):
        try:
            slots=cls.db.show_appointments_with_this_doctor(current_user)
        except DatabaseConnectionError:
            sys.exit(1)
        return slots

    # @property
    # def status(self):
    #     return self._status
    

