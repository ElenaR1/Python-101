import json
import operator
import sys
from random import *
import os


def read_json():
    with open('cars.json', 'r') as f:
        data = json.load(f)
    #print(data)
    return data

    return data

def make_car(data):
    cars=[]
    drivers=[]
    for person in data['people']:
        #print(person)
        car=Car(person['car'],person['model'],person['max_speed'])
        cars.append(car)
        drivers.append(Driver(person['name'],car))
    return drivers


class Car:
    def __init__(self,car,model,max_speed):#moje vmesto self da e rosi, prosto nadolu pak shte trqbva da e rosi;self e nashata instanciq, taka se zakacha
        self.car=car
        self.model=model
        self.max_speed=max_speed
    def __str__(self):
        s=self.car+' '+str(self.model)+' '+str(self.max_speed)
        return s
class Driver:
    def __init__(self,name,car):#moje vmesto self da e rosi, prosto nadolu pak shte trqbva da e rosi;self e nashata instanciq, taka se zakacha
        self.car=car
        self.name=name
        
    def __str__(self):
        s=self.name+' '+str(self.car)
        return s
class Race:
    def __init__(self,drivers,crash_chance):#moje vmesto self da e rosi, prosto nadolu pak shte trqbva da e rosi;self e nashata instanciq, taka se zakacha
        self.drivers=drivers
        self.crash_chance=crash_chance
        
    def __str__(self):
        s=self.name+' '+str(self.car)
        return s
    def result(self):
        points=[]
        maxx=max(self.crash_chance)
        ind=self.crash_chance.index(maxx)
        print('Unfortunately,'+self.drivers[ind].name+' has crashed.')
        self.drivers.remove(self.drivers[ind])
        

        n = len(self.drivers)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.drivers[j].car.max_speed > self.drivers[j+1].car.max_speed :
                    self.drivers[j], self.drivers[j+1] = self.drivers[j+1], self.drivers[j]
        self.drivers.reverse()
        # for ind,el in enumerate(self.drivers):
        #     if ind==0:
        #         points.append((el.name,8))
        #     if ind==1:
        #         points.append((el.name,6))
        #     if ind==2:
        #         points.append((el.name,4))
        #     if ind>2:
        #         points.append((el.name,0))
        # print('--------POINTS-----------')
        # print(points)
        return self.drivers
class Championship:
    points=[]
    def __init__(self,name,races_count):
        self.races_count=races_count
        self.name=name
        
    def top3(self):
        return self.points[:3]


def to_jason(el,indent=4):
        my_dict={}
        my_dict["dict:"]=el.__dict__
        my_dict["type"]=el.__class__.__name__
        y=json.dumps(my_dict,indent=indent)
        return y

def save(points):
        arr=[]
        my_dict={}
        for el in points:
            my_dict[el[0]]=el[1]
        # print(arr)
        name="result.json"
        path_to_folder=os.path.expanduser(os.path.join("~\python\week4/" + name))
        with open(path_to_folder, "a") as write_file:
            write_file.write(json.dumps(my_dict, indent=4))



def main():
    data=read_json()
    print('=========================')
    points=[]
    name=input()
    num_of_races=input()
    print('Starting a new championship called',name,' with', num_of_races,' races')
    print('Running',num_of_races,' races ...')
    ch=Championship(name,num_of_races)
    standings=[]
    drivers2=make_car(data)
    for i in range(int(num_of_races)):
        curr_points=[]
        print('-------------------------RACE #'+str(i+1)+' ----------------------------')
        # for dr in drivers2:
        #     print(dr)
        coeff=[]
        for j in range(len(drivers2)):
            x = uniform(0, 1) 
            coeff.append(x)
        #print(coeff)
        r=Race(drivers2,coeff)
        winners=r.result()# in result we remove one of the drivers 
        # for el in winners:
        #     print(el.name,el.car.__dict__)
        for ind,el in enumerate(winners):
            if ind==0:
                points.append((el.name,8))
                curr_points.append((el.name,8))
            if ind==1:
                points.append((el.name,6))
                curr_points.append((el.name,6))
            if ind==2:
                points.append((el.name,4))
                curr_points.append((el.name,4))
            if ind>2:
                points.append((el.name,0))
                curr_points.append((el.name,0))
        save(curr_points)
        print('--------POINTS-----------')
        for j in range(3):
            print(curr_points[j][0],'-',curr_points[j][1])
        # print('--------winners-----------')
        # for i in range(3):
        #     print(winners[i])
    print('==========Total championship standings:===========')
    final_points=[]
    #print(points)
    for i in range(len(points)//2):
        name=points[i][0]
        curr=points[i][1]
        for j in range(i+1,len(points)):
            #print(points[j][0])
            if points[j][0]==name:
                #print(name)
                curr+=points[j][1]
                #print(curr)
        final_points.append((name,curr))
    final_points.sort(key = operator.itemgetter(1))
    final_points.reverse()
    for el in final_points:
        ch.points.append(el)
    for el in final_points:
        print(el[0]+'-'+str(el[1]))
    print(ch.top3())


if __name__=='__main__':
    main()