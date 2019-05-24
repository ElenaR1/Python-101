# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy import create_engine
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import relationship


# Base = declarative_base()

# class BasicUser(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     user_name = Column(String)
#     password = Column(String)

#     def __str__(self):
#         return "{} - {}".format(self.id, self.name)

#     def __repr__(self):
#         return self.__str__()

# class Database():
#     engine = create_engine("sqlite:///hospital.db")
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     def __init__(self):

#         pass
#     @classmethod
#     def create_user(cls,user_name,password, type):
#         cls.session.add(BasicUser(user_name=user_name,password=password))
#         cls.session.commit()

    

import sqlite3
from database_layer.queries import *
class Database():
    def __init__(self):
        self.connection = sqlite3.connect('hospital.db')
        self.cursor = self.connection.cursor()

        #cursor.execute("ALTER TABLE BaseUser MODIFY COLUMN id Integer AUTO_INCREMENT ; ")

        #cursor.execute('DROP TABLE RepairHour')
        self.cursor.execute(CREATE_USER_TABLE)
        self.cursor.execute(CREATE_DOCTOR_TABLE)
        self.cursor.execute(CREATE_PATIENT_TABLE)
        self.cursor.execute(CREATE_SLOTS_TABLE)
        self.cursor.execute(CREATE_RESERVED_SLOTS_TABLE)
        self.connection.commit()
        
    def get_id(self,username):
        self.cursor.execute(GET_ID_OF_USER,(username,))
        id_user = self.cursor.fetchone()
        self.connection.commit()
        return id_user[0]
    # def get_id_of_user(self,current_user):
    #     user_id=self.get_id(current_user.username)
    #     if current_user.status=='d'
    #         self.cursor.execute(GET_ID_OF_DOCTOR,(user_id,))
    #         doc_id = self.cursor.fetchone()
    #         self.connection.commit()
    #         return doc_id[0]
    #     elif current_user.status=='p':
    #         self.cursor.execute(GET_ID_OF_PATIENT,(user_id,))
    #         doc_id = self.cursor.fetchone()
    #         self.connection.commit()
    #         return doc_id[0]
    def get_id_of_doctor(self,current_user):
        user_id=self.get_id(current_user.username)
        self.cursor.execute(GET_ID_OF_DOCTOR,(user_id,))
        doc_id = self.cursor.fetchone()
        self.connection.commit()
        return doc_id[0]
    def get_id_of_patient(self,current_user):
        user_id=self.get_id(current_user.username)
        self.cursor.execute(GET_ID_OF_PATIENT,(user_id,))
        patient_id = self.cursor.fetchone()
        self.connection.commit()
        return patient_id[0]
    def find_user(self,user_name,password):      
        self.cursor.execute(FIND_USER,(password,user_name))
        user = self.cursor.fetchone()
        self.connection.commit()
        return user
    def create_user(self,user_name,password,status,full_name):      
        self.cursor.execute(CREATE_USER.format(user_name=user_name,password=password,status=status,full_name=full_name))

        self.connection.commit()
    def create_doctor(self,title,current_user):
        id_user=self.get_id(current_user.username)      
        self.cursor.execute(CREATE_DOCTOR.format(title=title,id_user=id_user))
        self.connection.commit()
    def create_patient(self,address,age,unique_id,current_user):
        id_user=self.get_id(current_user.username)
        self.cursor.execute(CREATE_PATIENT.format(address=address,age=age,unique_id=unique_id,id_user=id_user))
        self.connection.commit()
    def add_slot(self,current_user,start_hour,end_hour,appointment_date,status):
        doctor_id=self.get_id_of_doctor(current_user)
        self.cursor.execute(CREATE_SLOT.format(start_hour=start_hour,end_hour=end_hour,appointment_date=appointment_date,
            status=status,doctor_id=doctor_id))
        self.connection.commit()
    def update_slot(self,slot_id,start_hour,end_hour):
        self.cursor.execute(UPDATE_SLOT_CHANGE_HOUR,(start_hour,end_hour,slot_id))
        self.connection.commit()
    def delete_slot(self,slot_id):
        self.cursor.execute(DELETE_SLOT,(slot_id,))
        self.connection.commit()
    def make_appointment(self,current_user,slot_id):
        patient_id=self.get_id_of_patient(current_user)
        self.cursor.execute(UPDATE_SLOT,(slot_id,))
        self.cursor.execute(CREATE_RESERVED_SLOT.format(status='pending',patient_id=patient_id,id_slot=slot_id))
        self.connection.commit()
    def cancel_appointment(self,slot_id):
        self.cursor.execute(UPDATE_SLOT_NOT_BOOKED,(slot_id,))
        self.cursor.execute(UPDATE_RESERVED_SLOT_CANCEL,(slot_id,))
        self.connection.commit()
    def delete_reserved_slot(self,slot_id):
        self.cursor.execute(DELETE_RESERVED_SLOT,(slot_id,))
        self.connection.commit()
    def change_status_to_done(self,slot_id):
        self.cursor.execute(UPDATE_RESERVED_SLOT_DONE,(slot_id,))
        self.connection.commit()
    def show_appointments_for_this_user(self,current_user):
        patient_id=self.get_id_of_patient(current_user)
        self.cursor.execute(SHOW_APPOINTMENTS_FOR_THIS_USER,(patient_id,))
        slots = self.cursor.fetchall()
        self.connection.commit()
        return slots
    def show_appointments_with_this_doctor(self,current_user):
        doctor_id=self.get_id_of_doctor(current_user)
        self.cursor.execute(SHOW_APPOINTMENTS_WITH_THIS_DOCTOR,(doctor_id,))
        slots = self.cursor.fetchall()
        self.connection.commit()
        return slots
    def list_all_free_slots(self):
         self.cursor.execute(LIST_ALL_FREE_SLOTS,('not booked',))
         slots = self.cursor.fetchall()
         self.connection.commit()
         return slots
    def list_all_booked_slots(self):
         self.cursor.execute(LIST_ALL_FREE_SLOTS,('booked',))
         slots = self.cursor.fetchall()
         self.connection.commit()
         return slots
    def list_slots(self,date_to_check):
         self.cursor.execute(LIST_SLOTS,('not booked',date_to_check))
         slots = self.cursor.fetchall()
         self.connection.commit()
         return slots
    def list_booked_slots(self,date_to_check):
         self.cursor.execute(LIST_BOOKED_SLOTS_FOR_SPECIFIC_DATE,('booked',date_to_check))
         slots = self.cursor.fetchall()
         self.connection.commit()
         return slots

# def main():
#     db=Database()
#     db.delete_reserved_slot(2)
# if __name__=='__main__':
#     main()