CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS User
                (id Integer  PRIMARY KEY AUTOINCREMENT, user_name Varchar UNIQUE ,password Varchar, status Varchar, full_name Varchar )
"""
CREATE_DOCTOR_TABLE = """CREATE TABLE IF NOT EXISTS Doctor
                (id_doc Integer  PRIMARY KEY AUTOINCREMENT, title Varchar ,id_user Integer, FOREIGN KEY (id_user) REFERENCES User(id) )
"""
CREATE_PATIENT_TABLE = """CREATE TABLE IF NOT EXISTS Patient
                (id_patient Integer  PRIMARY KEY AUTOINCREMENT, address Varchar ,age Integer,
                unique_id Integer UNIQUE ,id_user Integer, FOREIGN KEY (id_user) REFERENCES User(id) )
"""
CREATE_SLOTS_TABLE = """CREATE TABLE IF NOT EXISTS Slots
                (id_slot Integer  PRIMARY KEY AUTOINCREMENT, start_hour Varchar ,end_hour Varchar,
               appointment_date Varchar,status Varchar,doctor_id Integer,
                FOREIGN KEY (doctor_id) REFERENCES Doctor(id_doc) )
"""
CREATE_RESERVED_SLOTS_TABLE = """CREATE TABLE IF NOT EXISTS ReservedSlots
                (id_reserved_slot Integer  PRIMARY KEY AUTOINCREMENT, status Varchar,patient_id Integer,id_slot Integer,
                 FOREIGN KEY (patient_id) REFERENCES Patient(id_patient),
                FOREIGN KEY (id_slot) REFERENCES Slots(id_slot))
"""
CREATE_USER= """
            INSERT INTO User(user_name,password,status,full_name)  VALUES('{user_name}','{password}','{status}','{full_name}');
            """
CREATE_DOCTOR= """
            INSERT INTO Doctor(title,id_user)  VALUES('{title}','{id_user}');
            """
CREATE_PATIENT= """
            INSERT INTO Patient(address,age,unique_id,id_user)  VALUES('{address}','{age}','{unique_id}','{id_user}');
            """
CREATE_SLOT= """
            INSERT INTO Slots(start_hour,end_hour,appointment_date,status,doctor_id)  VALUES('{start_hour}','{end_hour}','{appointment_date}',
            '{status}','{doctor_id}');
            """
CREATE_RESERVED_SLOT= """
            INSERT INTO ReservedSlots(status,patient_id,id_slot)  VALUES('{status}','{patient_id}','{id_slot}');
            """
UPDATE_SLOT="""UPDATE Slots
                        SET status='booked'
                        WHERE id_slot = ? """
UPDATE_SLOT_NOT_BOOKED="""UPDATE Slots
                        SET status='not booked'
                        WHERE id_slot in (SELECT id_slot FROM ReservedSlots 
                                            WHERE id_reserved_slot = ?)
                        """

UPDATE_RESERVED_SLOT_CANCEL="""UPDATE ReservedSlots
                                SET status='cancel'
                                WHERE id_reserved_slot = ? """

SHOW_APPOINTMENTS_FOR_THIS_USER=""" SELECT id_reserved_slot, ReservedSlots.status, start_hour, end_hour, appointment_date,Slots.status,Doctor.title
                                     FROM  ReservedSlots
                                    JOIN Slots on Slots.id_slot=ReservedSlots.id_slot
                                    JOIN Doctor on Doctor.id_doc=Slots.doctor_id
                                    WHERE patient_id=?"""
UPDATE_RESERVED_SLOT_DONE="""UPDATE ReservedSlots
                                SET status='done'
                                WHERE id_reserved_slot = ? """
FIND_USER="""SELECT * FROM User WHERE password = ? and user_name = ?; """

GET_ID_OF_USER="""SELECT id FROM User WHERE user_name = ?; """ 
GET_ID_OF_DOCTOR="""SELECT id_doc FROM Doctor WHERE id_user = ?; """ 
GET_ID_OF_PATIENT="""SELECT id_patient FROM Patient WHERE id_user = ?; """               

LIST_ALL_FREE_SLOTS="""SELECT * FROM Slots WHERE status = ?;"""
LIST_ALL_BOOKED_SLOTS="""SELECT * FROM Slots WHERE status = ?;"""
LIST_SLOTS="""SELECT * FROM Slots WHERE status = ? and appointment_date=?;"""
LIST_BOOKED_SLOTS_FOR_SPECIFIC_DATE="""SELECT * FROM Slots WHERE status = ? and appointment_date=?;"""