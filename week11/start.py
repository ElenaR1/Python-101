import sys
from interface.start_menu import StartMenu

class Application:#this will be in the interface
    @classmethod
    def start(cls):
       StartMenu.run()

if __name__=='__main__':
    Application.start()