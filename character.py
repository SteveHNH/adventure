"""
Character
=========

Functions and classes that define what a character is and how it works.
"""


class Character:
    """
    Defines a character's race, class, and name. Later on we'll store this in
    some sort of file that we can use.

    Attributes::
        name(str): The name of the character
        race(str): The string of the character
        class(str): The class of the character

    Examples:
        >>> me = character.Character('boop', 'human', 'mage')
        >>> me.name
        'boop'
        >>> me.race
        'human'
        >>> me.class
        'mage'
    """

    def __init__(self, name, race, class_):
        self.name = name
        self.race = race
        self.class_ = class_


class Inventory:
    """
    Class to handle what is stored in the inventory, including additions and
    removals of items. Equipment will be managed in a different class to
    separate what is in use and what is just in the bag.
    """

    def __init__(self):

        self.bag = {}

        for i in ['slot1', 'slot2', 'slot3', 'slot4', 'slot5']:
            self.bag[i] = 'empty'

    def addToInv(item):
        return

    def removeFromInv(item):
        return

class Item:
    """
    Handle items in the game inluding gold, weapons, and items that can be used
    for a specific purpose.
    """

    def __init__(self, name, weight, value, type_):

        self.name = name
        self.weight = weight
        self.value = value
        self.type_ = type_


