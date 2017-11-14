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


class Item():
    """
    Handle items in the game inluding gold, weapons, and items that can be used
    for a specific purpose.
    """

    def __init__(self, name, description, value):

        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coind with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock suitable for bludgeoning",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust on the blade.",
                         value=10,
                         damage=10)
