from functools import wraps
from re import match, sub
from Logger import dlog, logs
from time import sleep
from random import randint
from Localizations import languages

# Logo
@dlog("printing the logo's separator")
def logo():
    logs(logo, 1, "printing the logo")
    print(r"""
 .          .                 .         .
    ___  _  _  ___       _     _  ___  _   _  ___ 
   |  _\| \| || _ \     | |   | |/  _\| |_| ||_ _|  *
   | |  |    || | |     | |__ | | (_ ||  _  | | | 
   |___/|_|\_||___/     |____||_|\___||_| |_| |_|
      *          .              *                .
    """)
    logs(logo, 1, "printing the logo's separator")
    print("=================================================")

# Separator
def separator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sep()
        return func(*args, **kwargs)
    return wrapper

def sep():
    print("====================================")

# Randomising value for the quest to be completed,
# if the value of the player's 'luck' is higher than
# the value it means that the quest has to be completed
@dlog("generating random number with random margins")
def random() -> int:
    return randint(randint(10, 20), randint(50, 70))

# Functions:
@dlog("game delay for better quality of game")
def sleep_delay(time_to_subtract: int = 0) -> None:
    if time_to_subtract == delay_time:
        logs(sleep_delay, 1, "standard delay")
        sleep(delay_time)
    elif time_to_subtract == delay_time_quest:
        logs(sleep_delay, 1, "quest delay")
        sleep(delay_time_quest)
    else:
        logs(sleep_delay, 1, "generic delay")
        sleep(delay_time - time_to_subtract if delay_time - time_to_subtract > 0 else delay_time)

@dlog("verifying whether the answer is positive or negative")
def verify_answer(string: str) -> bool|None:
    return match("Yes|yes|aha|Sure|OK|yeah|Yeah|y|Y|yep|Yep", sub(" ", "", string))

@dlog("choosing language for the game")
def language() -> str|None:
    print("Choose a language:")
    print("""1. English\t2. Polski\t3. Русский\t4. Державна\t5. НАДПОТУЖНА ДЕРЖАВНА""")
    def internal():
        try:
            logs(language, 1, "reading lang variable")
            while not (_lang := int(input("Enter a number from a list above: "))):
                logs(language, 1, "null lang")
                continue
            if not 1 <= _lang <= 5:
                logs(language, 1, "improper lang has been read")
                raise ValueError("Improper language has been chosen. Usage 1 <= lang <= 5")
            logs(language, 1, "lang has been read successfully")
            match _lang:
                case 1: return "en"
                case 2: return "pl"
                case 3: return "ru"
                case 4: return "ua"
                case 5: return "ua++"
        except ValueError:
            return internal()
    return internal()

@separator
@dlog()
def next_thing():
    @dlog("are we going forward?")
    def internal():
        if verify_answer(input(languages[lang]["next_thing"]["question"])):
            logs(next_thing, 1, "we are going forward")
            return True
        else:
            logs(next_thing, 1, "additional time to make decision")
            print(languages[lang]["next_thing"]["additional_time"])
            return internal()
    return internal()


# Global variables:
delay_time = 1
delay_time_quest = 1
lang = language()