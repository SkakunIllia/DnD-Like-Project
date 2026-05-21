from Entities import *
from Saver import *
from DeathException import DeathException
from Localizations import languages

#===================================================================================
# Generators
def gen_mob():
    mob_names = ["Zombie", "Skeleton", "Ogr", "Giant"]
    while True:
        yield Mob(mob_names[randint(0, len(mob_names) - 1)])

#===================================================================================
# Functions
@separator
@dlog("getting player's option to the quest")
def quest_get_option():
    try:
        while not (option := int(input(languages[lang]["quest_get_option"]))):
            logs(quest_get_option, 1, "null option")
            continue
        if not (1 <= option <= 3):
            logs(quest_get_option, 1, "improper option")
            raise ValueError("Wrong option. Usage: 1 <= player_class <= 3")
        return option
    except ValueError:
        return quest_get_option()

@dlog()
def quest_complete(luck, predicate):
    return predicate(luck)

@dlog()
def quest_is_successful(option):
    if option == 1:
        logs(quest_is_successful, 1, "option 1")
        return quest_complete(random(), lambda x: x > 0)
    elif option == 2:
        logs(quest_is_successful, 1, "option 2")
        return quest_complete(random(), lambda x: x > 50)
    else:
        logs(quest_is_successful, 1, "option 3")
        return quest_complete(random(), lambda x: x > 20)

@dlog()
@separator
def quest1(player):
    print(languages[lang]["quest1"][0])
    print(languages[lang]["quest1"][1]["desc"])
    sleep_delay(delay_time - 1)
    option = quest_get_option()
    is_successful = quest_is_successful(option)
    sep()
    logs(quest1, 1, f"is option successful? {is_successful}")

    def fight():
        sleep_delay(delay_time_quest)
        logs(fight, 1, "the player has started the fight")
        mob_counter = 3
        mobs = [next(gmob) for _ in range(mob_counter)]
        for i, mob in enumerate(mobs):
            sleep_delay(delay_time_quest)
            logs(fight, 2, f"player attack the mob {i}")
            player.attack(mob)
            if player.get_health() < 0:
                logs(fight, 2, "player has died")
                print(languages[lang]["quest1"][1]["fight"]["kill"])
                raise DeathException
        sleep_delay(delay_time_quest)
        logs(fight, 2, "player has won the fight")
        print(languages[lang]["quest1"][1]["fight"]["success"])
        player.add_item(Item("Diamond"))
        end_of_quest()

    def end_of_quest():
        sleep_delay(delay_time_quest)
        logs(end_of_quest, 2, "the player is outside the cave")

        print(languages[lang]["quest1"][1]["end_of_quest"]["1"])
        sleep_delay(delay_time_quest)
        print(languages[lang]["quest1"][1]["end_of_quest"]["2"])
        print(player)
        sleep_delay(delay_time)

    if option == 1:
        logs(quest1, 2, "the player leaves the quest")
        print(languages[lang]["quest1"][1]["options"]["1"])
    elif option == 2:
        logs(quest1, 2, "the player tries to sneak into the cave")
        if is_successful:
            sleep_delay(delay_time_quest)
            logs(quest1, 2, "the player sneaked into the cave successfully")
            print(languages[lang]["quest1"][1]["options"]["2"]["successful"])

            player.add(Item("Diamond"))
        else:
            logs(quest1, 2, "the player has been noticed while sneaking into the cave")
            print(languages[lang]["quest1"][1]["options"]["2"]["fail"])
            fight()
    elif option == 3:
        if is_successful:
            print(languages[lang]["quest1"][1]["options"]["3"]["successful"])
            fight()
        else:
            logs(quest1, 2, "the player has died in a fight")
            print(languages[lang]["quest1"][1]["options"]["3"]["fail"])
            raise DeathException

@separator
@dlog()
def quest2(player):
    pass

@separator
@dlog()
def main_location1(player):
    print(languages[lang]["main_locations"][0])
    sleep_delay(delay_time)

#===================================================================================
# Global variables

load_ingame_progres = load(None)
ingame_progress = load_ingame_progres if ((load_ingame_progres is not None) and (load_ingame_progres > 0)) else 0
game_quests = [main_location1, quest1]
gmob = gen_mob()

bin_file_to_extraction = 0

#===================================================================================
# Main game function
@dlog()
def game(player):
    hp = player.get_health()
    try:
        for i, location in enumerate(game_quests):
            if i < ingame_progress:
                continue
            location(player)
            if hp > 0 and (i + 1) % 2 == 0:
                if verify_answer(input(languages[lang]["game_save"])):
                    save(player)
            next_thing()
        end_of_game()
        if bin_file_to_extraction: input()
    except DeathException:
        death()

@separator
@dlog()
def end_of_game():
    sleep_delay(delay_time_quest)
    print(r"""
  _____ _    _ ______   ______ _   _ _____  
 |_   _| |  | |  ____| |  ____| \ | |  __ \ 
   | | | |__| | |__    | |__  |  \| | |  | |
   | | |  __  |  __|   |  __| | . ` | |  | |
   | | | |  | | |____  | |____| |\  | |__| |
   |_| |_|  |_|______| |______|_| \_|_____/
 """)

@dlog()
def death():
    end_of_game()