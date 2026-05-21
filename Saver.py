import json

from Logger import *
from Auxiliary import *
from Localizations import languages
from Entities import initialize_from_load

# Save Creater
@dlog()
def save(player):
    save_title = input(languages[lang]["saver_save"])
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
        res = verify_answer(input(languages[lang]["savefile_exists"]))
        if res:
            internal()
        else: save(player)
    else: internal()

# Save Loader
@dlog()
def load():
    def internal():
        try:
            while not (answer := int(input(languages[lang]["load"]))):
                continue
            nonlocal files
            if 1 <= answer < len(files) + 1:
                return answer - 1
            raise Exception
        except Exception:
            return internal()

    path_save = "saves/*.json"
    files = glob(path_save)
    if len(files) > 0:
        if verify_answer(input(languages[lang]["do_you_want_to_load"])):
            for i, file in enumerate(files):
                print(f"\t{i + 1}. {file}")
            answer = internal()
            file = files[answer]

            with open(file, "r") as file:
                obj = json.load(file)
            return initialize_from_load(obj)