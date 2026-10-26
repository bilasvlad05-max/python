

class hero:
    def __init__(self,name, hero_class,hp,attack):
        self.hero_class = hero_class
        self.name = name 
        self.hp = hp 
        self.attack = attack 
    def say_hello(self):
        print(f"darova! Я {self.name}")

    def show_card(self):
        print(f"Ім'я: {self.name}")
        print(f"Клас: {self.hero_class}")
        print(f"Здоров'я: {self.hp}")
        print(f"Атака: {self.attack}")

HULK = hero("галк","силач",400,350)
HULK.say_hello()


ARCHER = hero("Леголас", "Лучник", 250, 300)
MAGE = hero("Мерлін", "Маг", 200, 400)


ARCHER.show_card()
