from player import *
from random import randint
from time import sleep
from store import *
def fight():
    current_enemy = player["current_enemy"]
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]["hp"]
    print(f"Противник - {enemy['name']}: {enemy['talk']}")
    input("Enter чтобы продолжить")
    print()
    while player ['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            crit = randint(1, 100)
            if crit < player ['luck']:
                enemy_hp -= player['attack'] * 3
            else:
                    enemy_hp -= player['attack']
                    sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}')
            player["hp"] -= enemy["attack"] * player["armor"]
            sleep(1)
        print(f'''{player["name"]}: {player["hp"]}
        {enemy["name"]}: {enemy_hp}''')
        print()
        sleep(1)
        round += 1
        if player["hp"] > 0:
            print(f"Противник - {enemy['name']}:{enemy['win']}")
            player["current_enemy"] += 1
        else:
            print(f"Противник - {enemy['name']}: {enemy['win']}")
    player ['hp'] = 100
def training(training_type):
    for i in range(0,101,20):
        print(f"Тренировка завершена на {i}%")
        sleep(1.5)
    if training_type == "1":
        player["attack"] += 2
        print(f"Тренировка завершена! Теперь ваша атака равна {player['attack']}")
def inventory():
    count = 0
    for item in product:
        print(item["name"], item["price"])
        count += 1
    fabric = int(input("Введите индекс товара: "))
    player["inventory"].append(product[fabric])