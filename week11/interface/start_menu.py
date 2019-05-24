import sys
from controllers.main_controller import MainController
from interface.main_menu import MainMenu
class DatabaseConnectionError(Exception):
    pass
class UserAlreadyExistsError(Exception):
    pass
class PasswordsDontMatchError(Exception):
    pass
class StartMenu:
    #sign in & sign up
    #redirect to main menu
    @classmethod
    def run(cls):
        print('welcome to hospital hackbulgaria')
        options=""" 
        do you want to log in or to  create new profile?
        options:
        1-sign in
        2-sign up
        3 -exit
        """
        print(options)
        start_option=input()

        #todo check if it is diff than 1,2,3
        username=input('username-> ')
        password=input('password-> ')
        status=input('are you a doctor (d) or a patient (p) ? ')
        if start_option=='1':#the view communicates with the controller
            #todo hide psw
            current_user= MainController.sign_in(username,password)#return true or false
            if current_user:
                if status=='d':
                     MainMenu.show_options_for_doctor(current_user)
                elif status=='p':
                    MainMenu.show_options_for_patient(current_user)
            else:
                print('wrong username or password')
                sys.exit(1)#status 0,1 and -1
        elif start_option=='2':
            #TODO hide psq
            full_name=input('full_name-> ')
            second_password=input('repeat your password:')
            try:
                #raise 2 exceptions - user already exists, database connection error
                current_user=MainController.sign_up(username,password,second_password,status,full_name)
            except UserAlreadyExistsError:
                print('sign up failed. usr already exists')
                sys.exit(1)
            except DatabaseConnectionError:
                print('sign up failed. server error.try again')
                sys.exit(1)
            except PasswordsDontMatchError:
                print('sign up failed. psws dont match')
                sys.exit(1)
            else:
                #MainController.sign_in(username,password)
                #id_user=current_user.get_id()# put it in  database.py
                if current_user.status=='d':
                    title=input('title-> ')
                    MainController.add_doctor(title,current_user)
                    MainMenu.show_options_for_doctor(current_user)
                elif current_user.status=='p':
                    address=input('address-> ')
                    age=input('age-> ')
                    unique_id=input('unique_id-> ')
                    MainController.add_patient(address,age,unique_id,current_user)
                    MainMenu.show_options_for_patient(current_user)
        else:
            sys.exit(1)