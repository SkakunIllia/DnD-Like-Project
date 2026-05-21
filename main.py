from Game import *
from GameStart import *

@dlog()
def main():
    logo()
    player = load()
    if not player:
        sep()
        greeting()
        #
        print_player_classes()
        next_thing()
        print_player_classes_description()
        player = class_choice()

    game(player)
    # pass

main()