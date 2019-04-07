from money_tracker_menu import MoneyTrackerMenu
from parse_money_tracker_data import *
from aggregated_money_tracker import *


def main():
    arr=create_arr(sys.argv[1])#from parse_money_tracker
    my_dict=process_dict(arr)
    print(my_dict)
    a=AggregatedObject(my_dict)
    a.process()
    #print(a.all_user_data)
    mt_menu=MoneyTrackerMenu(a)
    mt_menu.option()




    # money_tr=MoneyTrackerMenu()
    # money_tr.option()

if __name__=='__main__':
    main()