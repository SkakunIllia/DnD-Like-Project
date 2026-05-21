from Entities import *
from Auxiliary import *
from Localizations import languages

@dlog("greeting the player")
def greeting():
    print(languages[lang]["greeting"])
    sleep_delay(delay_time)


@separator
@dlog("printing classes")
def print_player_classes():
    print(languages[lang]["print_player_classes"])
    sleep_delay(5)

@separator
@dlog("printing classes description")
def print_player_classes_description():
    print(languages[lang]["print_player_classes_description"].format(
        Archer.get_health(Archer(None)),
        Wizard.get_health(Wizard(None)),
        Gnome.get_health(Gnome(None)),
        Ogre.get_health(Ogre(None)),
        Knight.get_health(Knight(None))
    ))
    sleep_delay(7)

@separator
@dlog("reading player's name")
def read_player_name():
    while (player_name := input(languages[lang]["read_player_name"])) == "":
        logs(read_player_name, 1, "null name")
        continue
    return player_name

@dlog("reading player's class")
def read_player_class():
    try:
        while not (player_class := int(input(languages[lang]["read_player_class"]))):
            logs(read_player_class, 1, "null class")
            continue
        if not ( 1 <= player_class <= 5):
            logs(read_player_class, 1, "improper class")
            raise ValueError("Wrong player_class. Usage: 1 <= player_class <= 5")
        return player_class
    except ValueError:
        return read_player_class()

@dlog("choosing class")
def class_choice():
    player_name = read_player_name()
    player_class = read_player_class()
    logs(class_choice, 1, "initializing player")
    player = initialize_entity(player_class, player_name)
    print()
    sep()
    print(f"{languages[lang]["class_choice"]["character"]} {player.__repr__()}\n", end="")
    if verify_answer(input(languages[lang]["class_choice"]["accept_or_not?"])):
        logs(class_choice, 1, "going to the game itself")
        sep()
        print(languages[lang]["class_choice"]["accept"])
        return player
    else:
        logs(class_choice, 1, "rechoosing the class or the name")
        return class_choice()