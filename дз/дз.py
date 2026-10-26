import random

CLASSES = {
    "Воїн": {
        "hp": (100, 150),
        "attack": (15, 25)
    },
    "Маг": {
        "hp": (60, 100),
        "attack": (25, 40)
    },
    "Лучник": {
        "hp": (80, 120),
        "attack": (20, 35)
    }
}


def create_hero(name, hero_class):
    stats = CLASSES[hero_class]

    hero = {
        "name": name,
        "class": hero_class,
        "hp": random.randint(*stats["hp"]),
        "attack": random.randint(*stats["attack"])
    }

    return hero


def print_card(hero):
    print(f"Ім'я: {hero['name']}")
    print(f"Клас: {hero['class']}")
    print(f"HP: {hero['hp']}")
    print(f"Атака: {hero['attack']}")


hero = create_hero("Тінь", "Лучник")
print_card(hero)