from Person import Person
from hero import Hero
from enemy import Enemy
from potions import *
from abilities import *
import json
import random
from treasures import *
from fight import Fight



def main():
    h = Hero(name="Bron", title="Dragonslayer",
             health=100, mana=40, mana_regeneration_rate=2)
    print(h.known_as())
    print(h.get_health())
    h.take_damage(30)
    print('after damage')
    print(h.get_health())
    print(h.is_alive())
    print('after healing')
    print(h.take_healing(10))
    print(h.get_health())
    print('mana before taking potion')
    print(h.get_mana())

    w1 = Weapon("rifle", 50)
    s1 = Spell("invisibility", 20, 50, 2)
    h.equip(w1)
    w2 = Weapon("knife", 30)
    s2 = Spell("strength", 40, 20, 2)
    h.equip(w2)
    h.learn(s1)
    h.learn(s2)
    print('weapon damage:', h.current_weapon.damage)
    print('weapon damage:', h.damage_of_weapon())
    print('weapon damage:', h.attack("weapon"))
    print('spell damage:', h.attack("spell"))
    print('mana after an attack using spell which has 20 mana cost')
    print(h.get_mana())
    mp = ManaPotion("magic liquid", 20)
    h.take_mana(mp._mana)
    print('mana after taking potion that gives 20 mana')
    print(h.get_mana())

    e = Enemy(health=100, mana=100, damage=20)
    e.equip(w1)
    e.learn(s1)
    print('enemy attack: ', e.attack())
    print('enemy attack with a weapon: ', e.attack("weapon"))
    print('enemy attack with a spell: ', e.attack("spell"))

    print('----------FIGHT------------')
    f=Fight(h,e)
    print(f.log)
    print(f.won)

    print("============================")
    #pick_treasure()



if __name__ == '__main__':
    main()
