# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

class Panda:
    def __init__(self,name,food,weight,age):#moje vmesto self da e rosi, prosto nadolu pak shte trqbva da e rosi;self e nashata instanciq, taka se zakacha
        self.validate_init_params(name,food,weight,age)
        self.panda_name=name
        self.fav_food=food
        self.curr_weight=weight
        self.age=age



    def validate_init_params(self,name,food,weight,age):#self pokazva che e zakachen kum nashataa instannciq
        if name is str:
            print('panda_name is right')
        else:
            raise ValueError()

    def celebrate_birthday(self):
        self.age+=1




panda_ivo=Panda('Ivo','ice-cream',74,23)
print(panda_ivo.panda_name)
print(panda_ivo.fav_food)
print(panda_ivo.curr_weight)
panda_ivo.celebrate_birthday()
print(panda_ivo.age)


panda_rosi=Panda(20)
print(panda_rosi.panda_name)
