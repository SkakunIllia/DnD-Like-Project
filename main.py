import Entities

def print_player_classes():
    print("1. Archer")
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
        return player_class
    except ValueError:
        return read_player_class()

def main():
    player_name = read_player_name()
    print_player_classes()
    player_class = read_player_class()
    player = Entities.Player(player_name, player_class)
    print(player)


main()