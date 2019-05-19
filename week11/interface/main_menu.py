from tabulate import tabulate
from controllers.main_controller import MainController

class MainMenu:
    OPTION_MENU={
    '1':'_pretty_print_members'
    }

    @classmethod
    def default_method(cls,*args,**kwargs):
        print('HELP MENU')
    @staticmethod
    def show_slots(slots):
        arr=[]
        for el in slots:
            sub_arr=[el[0],el[1],el[2],el[3],el[4]]
            arr.append(sub_arr)
        print(tabulate(arr, headers=['id', 'start_hour','end_hour','date','status'], tablefmt='orgtbl'))
    @staticmethod
    def show_appointments(slots):
        arr=[]
        for el in slots:
            sub_arr=[el[0],el[1],el[2],el[3],el[4],el[5],el[6]]
            arr.append(sub_arr)
        print(tabulate(arr, headers=['res_slot','status', 'start_hour','end_hour','date','status','title'], tablefmt='orgtbl'))
    @classmethod
    def show_options_for_doctor(cls,current_user):
        flag=True
        while flag:
            print('1-list all free slots')
            print('2-list all free slots for a specific date')
            print('3-list all booked slots')
            print('4-list all booked slots for a specific date')
            print("5-add a slot")
            print("3-delete a slot")
            option=input()
            # method_name=cls.OPTION_MENU.get(option,cls.default_method)
            # method_name=getattr(cls,method_name)
            # method_name(**{})

            # if option=='1':
            #     members=MainController.show_members(current_user)
            #     cls._pretty_print_members(members)
            if option=='1':       
               free_slots=MainController.list_all_free_slots()
               cls.show_slots(free_slots)     
            if option=='2':
               date_to_check=input('date: ')
               slots=MainController.list_slots(date_to_check)
               cls.show_slots(slots) 
            if option=='3':       
               booked_slots=MainController.list_all_booked_slots()
               cls.show_slots(booked_slots) 
            if option=='4':
               date_to_check=input('date: ')
               slots=MainController.list_booked_slots(date_to_check)
               cls.show_slots(slots)           
            if option=='5':
               start_hour=input('start_hour: ')
               end_hour=input('end_hour: ')
               appointment_date=input('appointment_date: ')
               status=input('status: ')
               MainController.add_slot(current_user,start_hour,end_hour,appointment_date,status)
            if option=='exit':
                flag=False
    @classmethod
    def show_options_for_patient(cls,current_user):
        flag=True
        while flag:
            print('1-list all free slots')
            print('2-list all free slots for a specific date')
            print("3-make an appointmment")
            print("4-show appointments booked by this user")
            print("5-cancel an appointment")
            print("6-change the status of an appointment to 'done'")
            option=input()
            if option=='1':       
               free_slots=MainController.list_all_free_slots()
               cls.show_slots(free_slots)     
            if option=='2':
               date_to_check=input('date: ')
               slots=MainController.list_slots(date_to_check)
               cls.show_slots(slots) 
            if option=='3':
               slot_id=input('slot_id: ')
               MainController.make_appointment(current_user,slot_id)
            if option=='4':
               slots=MainController.show_appointments_for_this_user(current_user)
               cls.show_appointments(slots)
            if option=='5':
               slot_id=input('id of appointment you want to cancel: ')
               MainController.cancel_appointment(current_user,slot_id)
            if option=='6':
               slot_id=input('id of appointment you want to change: ')
               MainController.change_status_to_done(slot_id)
            if option=='exit':
                flag=False

    @classmethod
    def  _pretty_print_members(cls, members):
        for member in members:
            print('{status} {username}'.format(
                status=getattr(member, 'status', ''),
                username=member.username
            ))