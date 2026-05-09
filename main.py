import Entities
import logging
import os
from datetime import datetime
from glob import glob

def log():
    path = "logs/*.log"
    files = glob(path)
    if len(files) >= 5:
        os.remove(files[0])

    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    date_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".log"
    log_path = os.path.join(log_dir, date_now)
    logging.basicConfig(level = logging.DEBUG, filename = log_path, filemode = "w", format = "%(asctime)s - %(levelname)s - %(message)s")


def print_player_classes():
    print("1. Archer")
    print("2. Wizard")
    print("3. Gnome")
    print("4. Ogr")
    print("5. Knight")

def print_player_classes_description():
    print("1. Archer")
    print(f"\tYou posses a bow that can hit from a distance. Health: {Entities.Archer.get_health(Entities.Archer(None))}. "
          f"Damage: {Entities.Archer.get_damage(Entities.Archer(None))}")
    print("2. Wizard")
    print("3. Gnome")
    print("4. Ogr")
    print("5. Knight")

def read_player_name():
    while (player_name := input("What is your name? ")) == "":
        continue
    return player_name

def read_player_class():
    try:
        while not (player_class := int(input("What class do you want to play? (Enter a number) "))):
            continue
        if not ( 1 <= player_class <= 5):
            raise ValueError("Wrong player_class. Usage: 1 <= player_class <= 5")
        return player_class
    except ValueError:
        return read_player_class()

def greeting():
    print("Welcome to the game of D&D Light")
    print("The concept of the game is the same as in the D&D")
    print("The game consists of some random amount of quest that you have to complete")
    print("Then you enter the boss stage and that's all")
    print("Pretty simple, isn't it?")
    print("So let's try this game out!")

def separator():
    print("====================================")

def main():
    log()
    greeting()
    separator()
    print("Here are the classes that you can play in this game: ")
    print_player_classes()
    print("Each class has its own speciality")
    player_name = read_player_name()
    print_player_classes()
    player_class = read_player_class()
    player = Entities.Player(player_name, player_class)
    print(player)

main()