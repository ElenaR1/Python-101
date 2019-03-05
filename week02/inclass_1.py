# def gas_stations(distance, tank_size, stations):
#     newl=[]
#     i=0
#     n=len(stations)
#     while i < n:
#         for j in range(i+1,n-1):
#             dist=stations[j]-stations[i]
#             print("i: ",i,"j: ",j,"dist: ",dist)
#             # if(dist>tank_size):
#             #     print("dist in if: ",dist)
#             #     newl=newl+[stations[i]]+[stations[j-1]]
#             #     print("newl: ",newl)
#             #     i=j-1
#             #     

#         #i+1

#     return(newl)


#Is Number Balanced
def is_number_balanced(number):
    str_num=str(number)
    n=len(str_num)
    if(n%2!=0):


#print(is_number_balanced(9))

# def get_middle_char(str):
#     length = len(str)
#     return str[(length // 2) + (length % 2) - 1]

# print(get_middle_char("1234567"))
# print(get_middle_char("123456"))

 def gas_stations(distance, tank_size, stations):
     gas_stations_in_route=[]
     distance_traveled=0
     while True:
         if distance_traveled+tank_size>=distance:
             break
         gas_station=max([station for station in stations if station<=distance_traveled+tank_size])#tank_size vinagi go dobavqme i vinagi e 90
         gas_stations_in_route.append(gas_station)
         distance_traveled=gas_station

     return gas_stations_in_route


print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))

