import random 
CLASSES ={
   "Warior": {"hp":(110,140),"attack":(10,16)},
   "Drun": {"hp":(90,110),"attack":(40,45)},
   "kent": {"hp":(100,120),"attack":(26,30)}
}

def create_hero(name, hero_class):
    stats =CLASSES[hero_class]
    return{
        "name":name,
        "class":hero_class,
        "hp": random.randint(*stats["hp"]),
        "attack": random.randint(*stats["attack"])
    }

def show_hero(hero):
    print("="*30)
    print(f"Hero:{hero["name"]} - {hero["class"]}")
    print(f"HP: {hero["hp"]}")
    print(f"Attack: {hero["attack"]}")
    print("="*30)

hero = create_hero("drun", "Warior")
show_hero(hero)
# hero = {
#    "name":"Vladik",
#    "class":"big bro",
#    "hp": 100,
#    "attack": 50
# }

# print(hero["name"])

# if hero["hp"] <= 30:
#     print("gg")
# else:
#     print("ok")

# locations = ["даст", "міраж","еншент"]

# for l in locations:
#     print("локація:"+ l)

# def greetings():
#      print("привіт!")
# greetings()
# #доповнення
# classes = ["knight", "big bro", "small bro"]
# for c in classes:
#     print("classes:"+ c)

    