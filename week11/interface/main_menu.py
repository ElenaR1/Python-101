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
            print("5-add an appointment")
            print('6-show only your appointments')
            print('7-update an appointment')
            print("8-remove unbooked appointment")
            print("type exit if you want to exit the menu")
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
            if option=='6':
               slots=MainController.show_appointments_with_this_doctor(current_user)
               cls.show_slots(slots)
            if option=='7':
               slot_id=input('id of appointment you want to update:')
               start_hour=input('new start_hour: ')
               end_hour=input('new end_hour: ')
               MainController.update_slot(slot_id,start_hour,end_hour)
            if option=='8':
               slot_id=input('id of appointment you want to remove:')
               MainController.delete_slot(slot_id)
            if option=='exit':
                flag=False
    @classmethod
    def show_options_for_patient(cls,current_user):
        flag=True
        while flag:
            print('1-list all free slots')
            print('2-list all free slots for a specific date')
            print("3-make an appointmment")
            print("4-show appointments booked by you")
            print("5-cancel an appointment")
            print("6-change the status of an appointment to 'done'")
            print("7-delete a reserved slot'")
            print("type exit if you want to exit the menu")
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
               MainController.cancel_appointment(slot_id)
            if option=='6':
               slot_id=input('id of appointment you want to change: ')
               MainController.change_status_to_done(slot_id)
            if option=='7':
               slot_id=input('id of reserved_slot you want to delete: ')
               MainController.delete_reserved_slot(slot_id)
            if option=='exit':
                flag=False

    @classmethod
    def  _pretty_print_members(cls, members):
        for member in members:
            print('{status} {username}'.format(
                status=getattr(member, 'status', ''),
                username=member.username
            ))