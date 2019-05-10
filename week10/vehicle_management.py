import sqlite3
from tabulate import tabulate


def create_user_table():

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("ALTER TABLE BaseUser MODIFY COLUMN id Integer AUTO_INCREMENT ; ")

    #cursor.execute('DROP TABLE BaseUser')
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS BaseUser
            (id Integer  PRIMARY KEY, user_name Varchar UNIQUE ,email Varchar,
             phone_number Integer ,address Varchar )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Client
            (base_id Integer,
            FOREIGN KEY (base_id) REFERENCES BaseUser(id)
            )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Mechanic
            (base_id Integer,
             title Varchar ,
             FOREIGN KEY (base_id) REFERENCES BaseUser(id)
            )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Service
            (id Integer PRIMARY KEY,
             name Varchar 
            )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS MechanicService
            (id Integer PRIMARY KEY,
             mechanic_id Integer,
             service_id Integer,
             FOREIGN KEY (mechanic_id) REFERENCES Mechanic(base_id),
             FOREIGN KEY (service_id) REFERENCES Service(id)
            )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Vehicle
            (id Integer PRIMARY KEY,category Varchar, make Varchar, model Varchar,
             register_number Varchar, gear_box Varchar, owner Integer, 
             FOREIGN KEY (owner) REFERENCES Client(base_id)
            )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS RepairHour
            (id Integer PRIMARY KEY,repair_date Varchar, start_hour Varchar, vehicle Integer,
             bill Real, mechanic_service Integer, 
             FOREIGN KEY (vehicle) REFERENCES Vehicle(id),
             FOREIGN KEY (mechanic_service) REFERENCES MechanicService(id)
            )
        """
    )

    connection.commit()
    connection.close()
def check_if_user_is_in_db(user_name):#so it should be unique ?
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    query="SELECT * FROM BaseUser WHERE user_name = ?;"
    cursor.execute(query, (user_name,))
    user = cursor.fetchone()
    print('u',user)
    if user==None:
        return False
    else:
        return True
def add_baseuser(id,user_name,email,phone_number,address):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO BaseUser VALUES('{id}', '{user_name}','{email}','{phone}','{user_address}');
        """.format(id=id, user_name=user_name,email=email,phone=phone_number,user_address=address)
    )

    connection.commit()
    connection.close()
def add_client(base_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO Client VALUES('{base_id}');
        """.format(base_id=base_id)
    )

    connection.commit()
    connection.close()

def add_mechanic(base_id,title):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO Mechanic VALUES('{base_id}','{title}');
        """.format(base_id=base_id,title=title)
    )

    connection.commit()
    connection.close()
def add_service(id,name):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO Service VALUES('{id}','{name}');
        """.format(id=id,name=name)
    )

    connection.commit()
    connection.close()
def add_mechanic_service(id,mechanic_id,service_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO MechanicService VALUES('{id}','{mechanic_id}','{service_id}');
        """.format(id=id,mechanic_id=mechanic_id,service_id=service_id)
    )

    connection.commit()
    connection.close()
def add_vehicle(id,category,make,model,register_number,gear_box,owner):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO Vehicle VALUES('{id}','{category}','{make}','{model}','{register_number}','{gear_box}','{owner}');
        """.format(id=id,category=category,make=make,model=model,register_number=register_number,gear_box=gear_box,owner=owner)
    )

    connection.commit()
    connection.close()
def add_repair_hour(id,date,start_hour,vehicle,bill,mechanic_service):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO RepairHour VALUES('{id}','{date}','{start_hour}','{vehicle}','{bill}','{mechanic_service}');
        """.format(id=id,date=date,start_hour=start_hour,vehicle=vehicle,bill=bill,mechanic_service=mechanic_service)
    )

    connection.commit()
    connection.close()
def list():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Service")
    user = cursor.fetchall()

    connection.commit()
    connection.close()

    print(user)
def delete_user(id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute("DELETE FROM BaseUser WHERE id = ?;", (id,))

    connection.commit()
    connection.close()
def delete_repair_hour(id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute("DELETE FROM RepairHour WHERE id = ?;", (id,))

    connection.commit()
    connection.close()

def delete_client(id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute("DELETE FROM Client WHERE base_id = ?;", (id,))

    connection.commit()
    connection.close()

def list_all_free_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM RepairHour WHERE bill = ?;",('None',))
    hours = cursor.fetchall()

    connection.commit()
    connection.close()
    arr=[]
    for el in hours:
        sub_arr=[el[0],el[1],el[2]]
        arr.append(sub_arr)
    print(tabulate(arr, headers=['id', 'date','start_hour'], tablefmt='orgtbl'))
def list_free_hours(date_to_check):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM RepairHour WHERE bill = ? AND repair_date=?;",('None',date_to_check))
    hours = cursor.fetchall()

    connection.commit()
    connection.close()
    arr=[]
    for el in hours:
        sub_arr=[el[0],el[1],el[2]]
        arr.append(sub_arr)
    print(tabulate(arr, headers=['id', 'date','start_hour'], tablefmt='orgtbl'))




def main():
    create_user_table()
    #add_baseuser(1,'lili','lili_m@abv.bg',358659,'Sofia')
    #add_client(1)
    # add_baseuser(2,'petar','maya@petar_m@abv.bg.bg',56432,'Plovdiv')
    # add_baseuser(3,'maya','maya@abv.bg',6465,'Plovdiv')
    # add_baseuser(4,'ivan','petar_m@abv.bg',6457,'Sofia')
    # add_client(2)
    # add_baseuser(5,'todor','todor_m@abv.bg',6476,'Sofia')
    # add_mechanic(5,'auto mechanic')

    # add_service(1,'Basic Inspection')
    # add_service(2,'Oil change')
    # add_mechanic_service(1,4,1)
    # add_mechanic_service(2,5,2)
    # add_vehicle(1,'heavy car','fontaine modification','volvo authauler','678900A','bevel',1)
    # add_vehicle(2,'kit car','porsche','porsche 904','323900A','bevel',2)
    # add_repair_hour(1,'13-02-2019','15:00',1,100,1)
    # add_repair_hour(2,'14-02-2019','14:00',2,70,2)
    #add_repair_hour(3,'14-02-2019','16:00',None,None,None)
    #add_repair_hour(4,'15-02-2019','12:00',None,None,None)

    #list_all_free_hours()
    list_free_hours('15-02-2019')



    id=4

    # flag=True
    # while flag:
    #     print("Hello!")
    #     print("Provide user name:")
    #     user_name=input()
    #     if check_if_user_is_in_db(user_name)==False:
    #         print('Unknown user!')
    #         print('Would you like to create new user?')
    #         answer=input()
    #         if answer=='yes':
    #             print('Are you a client or Mechanic?')
    #             type_of_user=input()
    #             print('Provide user_name:')
    #             usr_name=input()
    #             print('Provide phone_number:')
    #             phone_number=input()
    #             print('Provide email:')
    #             email=input()
    #             print('Provide address:')
    #             address=input()
    #             add_baseuser(id+1,usr_name,email,phone_number,address)
    #             if type_of_user=='Client':
    #                 add_client(id+1)
    #             if type_of_user=='Mechanic':
    #                 print('Provide title:')
    #                 title=input()
    #                 add_mechanic(id+1,title)
    #             print('Thank you {}'.format(usr_name))
    #             print('Welcome to Vehicle Services!')
    #             print('Next time you try to login, provide your user_name!')
    #             flag=False
        

        

if __name__=='__main__':
    main()