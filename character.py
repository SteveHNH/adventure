"""
Character
=========

Functions and classes that define what a character is and how it works.
"""


class Character:

    def __init__(self, name, race, class_):
        self.name = name
        self.race = race
        self.class_ = class_


class Inventory:

    def __init__(self):

        self.bag = {}

        for i in ['slot1', 'slot2', 'slot3', 'slot4', 'slot5']:
            self.bag[i] = 'empty'

    def addToInv(item):
        return

    def removeFromInv(item):
        return

