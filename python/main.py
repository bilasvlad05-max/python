

class hero:
    def __init__(self,name, hero_class,hp,attack):
        self.hero_class = hero_class
        self.name = name 
        self.hp = hp 
        self.attack = attack 
    def say_hello(self):
        print(f"darova! Я {self.name}")
    def hit(self, target):
        print(f"{self.name} наносить удар {target.name} і наносить {self.attack} шкоди")
        target.take_damage(self.attack)
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp > 0:
            print("Ти живий,залишилось{self.hp}")
        else:
            print("Героя переможено")

spider_man = hero("Людина-павук","Боєць",120,120)
venom = hero("Venom","Alien",200,80)
spider_man.hit(venom)
spider_man.hit(venom)

    # def show_card(self):
    #     print(f"Ім'я: {self.name}")
    #     print(f"Клас: {self.hero_class}")
    #     print(f"Здоров'я: {self.hp}")
    #     print(f"Атака: {self.attack}")

HULK = hero("галк","силач",400,350)
HULK.say_hello()


ARCHER = hero("Леголас", "Лучник", 250, 300)
MAGE = hero("Мерлін", "Маг", 200, 400)


# ARCHER.show_card()


# class enemy:
#     def __init__(self,name, hp,attack ):
#         self.name = name
#         self.hp = hp
#         self.attck = attack

