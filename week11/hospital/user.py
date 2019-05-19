from hospital.database import Database
class DatabaseConnectionError(Exception):
    pass

class User:
    db=Database()

    def __init__(self,username,password,status=None,full_name=None):
        self.username=username
        self.password=password
        print('status',status)
        self.status=status
        self.full_name=full_name
        print(self.status,self.full_name)

    @classmethod
    def find(cls,username,password):#we make the connection to the databaselayer
        result=cls.db.find_user(username,password)
        if result:#if it is None or [] it wont proceed
            return cls(username,password,result[3],result[4])
    def get_id(self):
        return self.db.get_id(self.username)

    @classmethod
    def create_new_user(cls,username,hashed_pass, **kwargs):
        try:
            cls.db.create_user(username,hashed_pass,**kwargs)
        except DatabaseConnectionError:
            sys.exit(1)
        return cls(username,hashed_pass,**kwargs)
    @classmethod
    def list_all_free_slots(cls):
        try:
            free_slots=cls.db.list_all_free_slots()
        except DatabaseConnectionError:
            sys.exit(1)
        return free_slots
    @classmethod
    def list_all_booked_slots(cls):
        try:
            booked_slots=cls.db.list_all_booked_slots()
        except DatabaseConnectionError:
            sys.exit(1)
        return booked_slots
    @classmethod
    def list_slots(cls,date_to_check):
        try:
            slots=cls.db.list_slots(date_to_check)
        except DatabaseConnectionError:
            sys.exit(1)
        return slots
    @classmethod
    def list_booked_slots(cls,date_to_check):
        try:
            slots=cls.db.list_booked_slots(date_to_check)
        except DatabaseConnectionError:
            sys.exit(1)
        return slots
    # @property
    # def status(self):
    #     return self._status
    

