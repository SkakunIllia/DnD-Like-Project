from random import randint

# Randomising value for the quest to be completed,
# if the value of the player`s 'luck' is higher than
# the value it means that the quest has to be completed
def random():
    return randint(40, 70)

class Entity:
    def __init__(self, name, type):
        self._name = name
        self._type = type
    def __repr__(self):
        return f'Entity[Name: {self._name}, type: {self._type}]'

class Player(Entity):
    def __init__(self, name, player_class):
        super().__init__(name, "Player")
        self._player_class = player_class
    def __repr__(self):
        return f'Player[Name: {self._name}, type: {self._type}, player class: {self._player_class}]'

class Item(Entity):
    def __init__(self, name):
        super().__init__(name, "Item")
    def __repr__(self):
        return f'Item[Name: {self._name}, type: {self._type}]'

class Quest:
    def __init__(self, name):
        self._name = name
        self._random_value = random()
    def __repr__(self):
        return f'Item[Name: {self._name}, random value: {self._random_value}]'