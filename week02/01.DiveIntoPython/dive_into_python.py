import sys

def to_digits2(n):
    n = abs(n)

    return [int(ch) for ch in str(n)]#The str() method returns the "informal" or nicely printable representation of a given object.
print(to_digits2(123))

def gas_stations(distance,tank_size,stations):
    gas_stations_in_route=[]
    distance_traveled=0
    while True:
        if distance_traveled+tank_size>=distance:
            break
        #print([station for station in stations if station<=distance_traveled+tank_size])
        gas_station=max([station for station in stations if station<=distance_traveled+tank_size])
        gas_stations_in_route.append(gas_station)
        distance_traveled=gas_station

    return gas_stations_in_route
print('====Gas stations======')
print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))


#Is Number Balanced
print("======Is Number Balanced======")
def is_number_balanced(number):
    num_str=str(number)
    n=len(num_str)
    middle=n//2
    sum_left=0
    sum_right=0
    if(len==1):
        return True
    if n%2 == 0:        
        for i in range(0,middle):
            #print(num_str[i])
            sum_left=sum_left+int(num_str[i])
        for i in range(middle,n):
            #print(num_str[i])
            sum_right=sum_right+int(num_str[i])
    else:
        for i in range(0,middle):
            #print(num_str[i])
            sum_left=sum_left+int(num_str[i])
        for i in range(middle+1,n):
            #print(num_str[i])
            sum_right=sum_right+int(num_str[i])
    return sum_left==sum_right

print('9',is_number_balanced(9))
print('45318',is_number_balanced(45318))
print('28471',is_number_balanced(28471))
print('1238033',is_number_balanced(1238033))
print('23567414',is_number_balanced(23567414))




#Increasing and Decreasing Sequences
print("====Increasing and Decreasing Sequences======")

def inc(lst):
    n=len(lst)
    count=0
    for i in range(n-1):
        if lst[i]<lst[i+1] and lst[i]!=lst[i+1]:
            count=count+1
    if count == n-1:
        return True
    else:
        return False

def dec(lst):
    n=len(lst)
    count=0
    for i in range(n-1):
        if lst[i]>lst[i+1] and lst[i]!=lst[i+1]:
            count=count+1
    if count == n-1:
        return True
    else:
        return False

def increasing_or_decreasing(seq):
    n=len(seq)
    if inc(seq)==True:
        return "Up"
    if dec(seq)==True:
        return "Down"
    else:
        return False

print(increasing_or_decreasing([1,2,3,4,5]))
print(increasing_or_decreasing([5,6,-10]))
print(increasing_or_decreasing([1,1,1,1]))
print(increasing_or_decreasing([9,8,7,6]))

#Largest Palindrome
print('=======Largest Palindrome=======')

def get_largest_palindrome(num):
    numstr = str(num)
    for i in reversed(range(num)):#sys.min; negative numbers
        #print(str(i),str(i)[::-1])
        if str(i) == str(i)[::-1]:
            return i

print(get_largest_palindrome(9))
print(get_largest_palindrome(99))
print(get_largest_palindrome(252))
print(get_largest_palindrome(994687))
print(get_largest_palindrome(754649))


#Sum all numbers in a given string
print('======Sum all numbers in a given string======')
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def sum_of_numbers(input_string):
    temp=''
    sum=0
    if hasNumbers(input_string)==False:
        return 0
    for index,ch in enumerate(input_string):
        if ch.isdigit():
            #print(ch,temp)
            temp=temp+ch
        if ch.isdigit()==False:
            #print(ch)
            if(temp.isdigit()):
                #print(ch,temp)
                temp_num=int(temp)# int('x') ValueError: invalid literal for int() with base 10: 'x'
                sum=sum+temp_num
                temp=''
        if(ch.isdigit and index==len(input_string)-1 and temp.isdigit()):
             #print("end" ,temp)
             sum= sum+int(temp)
    return sum
   

print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
print(sum_of_numbers("1101"))
print(sum_of_numbers("1111O"))
print(sum_of_numbers("1abc33xyz22"))
print(sum_of_numbers("0hfabnek"))
print(sum_of_numbers("2h3a0nek"))



#Birthday Ranges
print('======Birthday Ranges======')
def birthday_ranges(birthdays, ranges):
    count_lst=[]
    count=0
    for item in ranges:
        for birthday in birthdays:
            if birthday>=item[0] and birthday<=item[1]:
                count=count+1
        count_lst=count_lst+[count]
        count=0
    return count_lst


l=[(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]
print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))#[2, 3, 4, 5, 2]
print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))#[2, 3, 4, 5, 2]



print('=========100 SMS===========')
buttons = {
        0: ' ',
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }


def numbers_to_message(pressed_sequence):
    msg = ""
    count_equal_digits = 0
    is_capital = False

    for index in range(1, len(pressed_sequence)):

        if pressed_sequence[index - 1] == 1:
            is_capital = True

        elif pressed_sequence[index - 1] == -1:
            count_equal_digits = 0

        elif pressed_sequence[index - 1] != pressed_sequence[index]:
            if count_equal_digits > len(buttons[pressed_sequence[index - 1]]) - 1:
                #print('======repeating=============')
                count_equal_digits = 0
           
            if is_capital==False:
                dig=pressed_sequence[index - 1]
                msg += buttons[dig][count_equal_digits]
            if is_capital==True:
                dig=pressed_sequence[index - 1]
                msg += buttons[dig][count_equal_digits].upper()
                is_capital = False

            if index == len(pressed_sequence) - 1:
                dig=pressed_sequence[index]
                msg += buttons[dig][count_equal_digits] 

            count_equal_digits = 0
        else:
            count_equal_digits += 1
            if index == len(pressed_sequence) - 1:
                if count_equal_digits > len(buttons[pressed_sequence[index - 1]]) - 1:
                    #print('rep')
                    count_equal_digits = 0
                if is_capital==False:
                    dig=pressed_sequence[index - 1]
                    msg += buttons[dig][count_equal_digits]
                if is_capital==True:
                    dig=pressed_sequence[index - 1]
                    msg += buttons[dig][count_equal_digits].upper()
                    is_capital = False
    return msg

print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
print(numbers_to_message([2, 2, 2, 2]))
print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))

print('=======Elevator Trips========')
def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    if people_weight==[] or people_floors==[]:
        return 0
    trips=0
    current_weight=0
    start=0
    for index,person_weight in enumerate(people_weight):
        current_weight+=person_weight
       # print(start,index,people_weight[start:index])
        if current_weight>max_weight or len(people_weight[start:index])>=max_people : #or len(people_weight)==index+1:#people_floors[0:3]->[
            #print(start,index,set(people_floors[start:index]),len(set(people_floors[start:index]))+1)
            trips+=len(set(people_floors[start:index]))+1
            current_weight=person_weight
            start=index
    #print(start,index,people_floors[start:])
    trips+=len(set(people_floors[start:]))+1
    return trips

def elevator(people_weight, people_floors, elevator_floors, max_people, max_weight):
    if people_weight==[] or people_floors==[]:
        return 0
    trips=0
    while len(people_weight)>0:
        current_floors=[people_floors[index] for index,person in enumerate(people_weight)
                        if sum(people_weight[:index+1])<max_weight
                        and len(people_weight[:index+1])<=max_people]
        trips+=len(set(current_floors))+1
        people_weight=people_weight[len(current_floors):]
        people_floors=people_floors[len(current_floors):]

    return trips


print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))
print(elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200))
print(elevator_trips([], [], 5, 2, 200))
print(elevator_trips([40, 50], [], 5, 2, 200))

print(elevator([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))
print(elevator([80, 60, 40], [2, 3, 5], 5, 2, 200))
print(elevator([], [], 5, 2, 200))
print(elevator([40, 50], [], 5, 2, 200))