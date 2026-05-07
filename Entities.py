from random import randint

def random():
    return randint(40, 70)

class Entity:
    def __init__(self, name, type):
        self._name = name
        self._type = type
    def __repr__(self):
        return f'Entity[Name: {self._name}, type: {self._type}]'

class Player(Entity):
    def __init__(self, name):
        super().__init__(name, "Player")
    def __repr__(self):
        return f'Player[Name: {self._name}, type: {self._type}]'

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