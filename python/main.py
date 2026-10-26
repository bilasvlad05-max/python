import random

print(random.randinr(0,6000))

class hero:
    def __init__(self,name, hero_class,hp,attack):
        self.hero_class = hero_class
        self.hp = hp 
        self.attack = attack 
def say_hello(self):
    print(f"darova! Я {self.name}")

HULK = hero("галк","силач",400,350)
HULK.say_hello()