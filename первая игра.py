from random import randint
from time import sleep
from fight import *
name = input("Введите своё имя героя: ")
player["name"] = name
while True:
    action = input("""Действие:
1 - Бой
2 - Тренировка
3 - Магазин                  
"""   )
    if action == "1":
        fight()
    elif action == "2":
        training_type = input('''1 - тренировать атаку ''')
        training(training_type)
    elif action == "3":
        inventory()
        print (player)