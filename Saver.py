import json, os
from Logger import *
from Auxiliary import *
from Dialogues import languages

# Save Creater
@dlog()
def save(player):
    save_title = input("How would you like to name the save file? ")
    save_dir = "saves"

    def internal():
        nonlocal save_dir, player
        path = save_title + ".json"
        save_file = os.path.join(save_dir, path)
        obj = player.serialize()
        with open(save_file, "wt") as file:
            json.dump(obj, file, indent = 4)


    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    path_save = "saves/*.json"
    files = glob(path_save)
    if "saves/" + save_title + ".json" in files:
        print("The file with this name already exists")
        res = verify_answer(input("Do you want to override the save file? "))
        if res:
            internal()
        else: save(player)
    else: internal()

# Save Loader
@dlog()
def load(save_file):
    pass

    # with open("saves/save1.json", "r") as file:
    #     obj = json.load(file)
    # print(obj)
    # item = eval(obj["items"][0])
    # print(item)
    # to be continued