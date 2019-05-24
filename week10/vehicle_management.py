import sqlite3
from tabulate import tabulate

def create_user_table():

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    #cursor.execute("ALTER TABLE BaseUser MODIFY COLUMN id Integer AUTO_INCREMENT ; ")

    #cursor.execute('DROP TABLE RepairHour')
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS BaseUser
            (id Integer  PRIMARY KEY AUTOINCREMENT, user_name Varchar UNIQUE ,email Varchar,
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
            (id Integer PRIMARY KEY AUTOINCREMENT,category Varchar, make Varchar, model Varchar,
             register_number Varchar, gear_box Varchar, owner Integer, 
             FOREIGN KEY (owner) REFERENCES Client(base_id)
            )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS RepairHour
            (id Integer PRIMARY KEY AUTOINCREMENT,repair_date Varchar, start_hour Varchar, vehicle Integer,
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
def add_baseuser(user_name,email,phone_number,address):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO BaseUser(user_name, email, phone_number, address)  VALUES('{user_name}','{email}','{phone}','{user_address}');
        """.format(user_name=user_name,email=email,phone=phone_number,user_address=address)
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
def add_vehicle(category,make,model,register_number,gear_box,owner):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO Vehicle(category,make,model,register_number,gear_box,owner) 
        VALUES('{category}','{make}','{model}','{register_number}','{gear_box}','{owner}');
        """.format(category=category,make=make,model=model,register_number=register_number,gear_box=gear_box,owner=owner)
    )

    connection.commit()
    connection.close()

def add_repair_hour(repair_date,start_hour,vehicle='None',bill='None',mechanic_service='None'):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO RepairHour(repair_date,start_hour,vehicle,bill,mechanic_service)  VALUES('{repair_date}','{start_hour}','{vehicle}','{bill}','{mechanic_service}');
        """.format(repair_date=repair_date,start_hour=start_hour,vehicle=vehicle,bill=bill,mechanic_service=mechanic_service)
    )

    connection.commit()
    connection.close()
def get_id_of_user(user_name):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query="SELECT id FROM BaseUser WHERE user_name = ?;"
    cursor.execute(query, (user_name,))
    user = cursor.fetchone()

    connection.commit()
    connection.close()

    return user[0]
def get_type_of_user(id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query="SELECT COUNT(*) FROM Client WHERE base_id = ?;"
    cursor.execute(query, (id,))
    user = cursor.fetchone()

    connection.commit()
    connection.close()

    if user[0]!=0:
        return 'Client'
    else:
        connection = sqlite3.connect('vehicle_management.db')
        cursor = connection.cursor()

        query="SELECT COUNT(*) FROM Mechanic WHERE base_id = ?;"
        cursor.execute(query, (id,))
        user = cursor.fetchone()

        connection.commit()
        connection.close()
        if user[0]!=0:
            return 'Mechanic'


    
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
def delete_vehicle(id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute("DELETE FROM Vehicle WHERE id = ?;", (id,))

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
def list_all_busy_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM RepairHour WHERE bill IS NOT ?;",('None',))
    hours = cursor.fetchall()

    connection.commit()
    connection.close()
    arr=[]
    for el in hours:
        sub_arr=[el[0],el[1],el[2]]
        arr.append(sub_arr)
    print(tabulate(arr, headers=['id', 'date','start_hour'], tablefmt='orgtbl'))
def list_busy_hours(date_to_check):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM RepairHour WHERE bill IS NOT ? AND repair_date=?;",('None',date_to_check))
    hours = cursor.fetchall()

    connection.commit()
    connection.close()
    arr=[]
    for el in hours:
        sub_arr=[el[0],el[1],el[2]]
        arr.append(sub_arr)
    print(tabulate(arr, headers=['id', 'date','start_hour'], tablefmt='orgtbl'))

def update_tbl(tbl_name,_id,to_change,val):
    print(to_change,val)
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    cursor.execute(f"""UPDATE {tbl_name} 
                       SET {to_change} = '{val}'
                       WHERE id={_id};""")

    hours = cursor.fetchone()
    connection.commit()
    connection.close()    
def show_repair_hour(id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute("""SELECT repair_date,start_hour,user_name,make,model,bill FROM RepairHour
                     JOIN Vehicle ON Vehicle.id=RepairHour.vehicle 
                     JOIN BaseUser ON Vehicle.owner=BaseUser.id 
                     WHERE RepairHour.id = ?;""",(id,))
    hours = cursor.fetchone()
    connection.commit()
    connection.close()
    #print(hours)
    msg=f"""On {hours[0]} at {hours[1]}: \nClient: {hours[2]} \nVehicle:
     {hours[3]} {hours[4]} \nCurrent Bill: {hours[5]}$"""
    print(msg)
    print('Choose one of the following:')
    print("""1 - change start hour \n2 - change bill \n3 - return to main menu""")
    choice=input()
    to_change=""
    if choice=='1':
        to_change='start_hour'
        print(f"Current start hour is {hours[1]}")
        print('New start hour is:')
        val=input()
    if choice=='2':
        to_change='bill'
        print(f"Current bill is {hours[5]}")
        print('New Bill:')
        val=input()
    update_tbl('RepairHour',id,to_change,str(val))
def show_vehicle(id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute("""SELECT user_name,category,make,model,register_number,gear_box FROM Vehicle 
                     JOIN BaseUser ON Vehicle.owner=BaseUser.id 
                     WHERE Vehicle.id = ?;""",(id,))
    veh = cursor.fetchone()
    connection.commit()
    connection.close()
    msg=f"""Client: {veh[0]} \nVehicle: {veh[1]} {veh[2]} {veh[3]} \nRegister number: {veh[4]} \nGear box: {veh[5]} """
    print(msg)
    print('Choose one of the following:')
    print("""1 - change category \n2 - change make \n3 - change model \n4 - change register_number \n5 change gear_box
     \n6 - return to main menu""")
    choice=input()
    to_change=""
    if choice=='1':
        to_change='category'
        print(f"Current category is {veh[1]}")
        print('New category is:')
        val=input()
    if choice=='2':
        to_change='make'
        print(f"Current make is {veh[2]}")
        print('New make:')
        val=input()
    if choice=='3':
        to_change='model'
        print(f"Current model is {veh[3]}")
        print('New model:')
        val=input()
    if choice=='4':
        to_change='register_number'
        print(f"Current register_number is {veh[4]}")
        print('New register_number:')
        val=input()
    if choice=='5':
        to_change='gear_box'
        print(f"Current gear_box is {veh[5]}")
        print('New gear_box:')
        val=input()
    update_tbl('Vehicle',id,to_change,val)
def save_repair_hour(hour_id):
    print('Vehicle:')
    vehicle =input()
    print('mechanic_service:')
    mechanic_service=input()

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()


    cursor.execute(F"""UPDATE RepairHour
                        SET vehicle={vehicle}, mechanic_service={mechanic_service}
                        WHERE id={hour_id};""")
    vehicles = cursor.fetchall()

    connection.commit()
    connection.close()
    # arr=[]
    # for el in vehicles:
    #     msg=el[1]+' '+el[2]+' with RegNumber: '+el[3]
    #     sub_arr=[el[0],msg]
    #     arr.append(sub_arr)
    # print(tabulate(arr, headers=['id', 'Vehicle'], tablefmt='orgtbl'))


def main():
    create_user_table()
    #add_baseuser('lili','lili_m@abv.bg',358659,'Sofia')
    #add_client(1)
    # add_baseuser('petar','maya@petar_m@abv.bg.bg',56432,'Plovdiv')
    # add_baseuser('maya','maya@abv.bg',6465,'Plovdiv')
    # add_baseuser('ivan','petar_m@abv.bg',6457,'Sofia')
    # # add_client(2)
    #add_baseuser('todor','todor_m@abv.bg',6476,'Sofia')
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
    # list_free_hours('15-02-2019')
    # save_repair_hour(3)

    added=False
    flag=True
    while flag:
        print("Hello!")
        print("Provide user name:")
        user_name=input()
        if check_if_user_is_in_db(user_name)==False:
            print('Unknown user!')
            print('Would you like to create new user?')
            answer=input()
            if answer=='no':
                break
            if answer=='yes':
                print('Are you a client or Mechanic?')
                type_of_user=input()
                print('Provide user_name:')
                usr_name=input()
                print('Provide phone_number:')
                phone_number=input()
                print('Provide email:')
                email=input()
                print('Provide address:')
                address=input()
                add_baseuser(usr_name,email,phone_number,address)
                id=get_id_of_user(usr_name)
                if type_of_user=='Client':
                    add_client(id)
                if type_of_user=='Mechanic':
                    print('Provide title:')
                    title=input()
                    add_mechanic(id,title)
                print('Thank you {}'.format(usr_name))
                print('Welcome to Vehicle Services!')
                print('Next time you try to login, provide your user_name!')
        id=get_id_of_user(user_name)
        user_type=get_type_of_user(id)
        inner_flag=True
        while inner_flag:
            print('You can choose from the following commands:')
            print('1 list_all_free_hours')
            print('2 list_free_hours <date>')
            if user_type=='Client':
                print('3 save_repair_hour <hour_id>')
                print('4 update_repair_hour <hour_id>')
                print('5 delete_repair_hour <hour_id>')
                print('6 list_personal_vehicles')
                print('7 add_vehicle')
                print('8 update_vehicle <vehicle_id>')
                print('9 delete_vehicle <vehicle_id>')
            if user_type=='Mechanic':
                print('3 list_all_busy_hours')
                print('4 list_busy_hours <date>')
                print('5 add_new_repair_hour')
                print('6 add_new_service')
                print('7 update_repair_hour <hour_id>')
            print('exit')
            command=input()
            if command=='1':
                list_all_free_hours()
            if command=='2':
                print('Date:')
                date=input()
                list_free_hours(date)
            if command=='3' and user_type=='Client':
                print('hour id:')
                hour_id=input()
                save_repair_hour(hour_id)
            if command=='3' and user_type=='Mechanic':
                list_all_busy_hours()
            if command=='4' and user_type=='Client':
                print('hour id:')
                hour_id=input()
                show_repair_hour(hour_id)
            if command=='4' and user_type=='Mechanic':
                print('Date:')
                date=input()
                list_busy_hours(date)
            if command=='5' and user_type=='Client':
                print('hour id:')
                hour_id=input()
                delete_repair_hour(hour_id)
            if command=='5' and user_type=='Mechanic':
                print('Date:')
                _date=input()
                print('start_hour:')
                start_hour =input()                
                add_repair_hour(_date,start_hour)
            if command=='7':
                print('Vehicle category:')
                category=input()
                print('Vehicle make:')
                make=input()
                print('Vehicle model:')
                model=input()
                print('Vehicle register number:')
                register_number=input()
                print('Vehicle gear box:')
                gear_box=input()
                add_vehicle(category,make,model,register_number,gear_box,id)
            if command=='8':
                print('vehicle id:')
                vehicle_id=input()
                show_vehicle(vehicle_id)
            if command=='9':
                vehicle_id=input()
                delete_vehicle(vehicle_id)
            if command=='exit':
                inner_flag=False
        flag=False


        

if __name__=='__main__':
    main()