import os
from character import Character
from character import Inventory

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def class_list():
    classes = ['mage',
               'warrior',
               'rogue',
               'cleric']
    return classes


def race_list():
    races = ['human',
             'elf',
             'dwarf',
             'gnome']
    return races


def character_init():
    the_name = None
    the_race = None
    the_class = None
    print("\nChoose your race from this list: ")
    for i in race_list():
        print(i)
    while the_race is None:
        the_race = raw_input('\nSelection: ')
        if not the_race.lower() in race_list():
            the_race = None
            print("Please choose a race from the list")
    print("\nChoose your class from this list: ")
    for i in class_list():
        print(i)
    while the_class is None:
        the_class = raw_input("\nSelection: ")
        if not the_class.lower() in class_list():
            the_class = None
            print("Please choose a class from the list")
    print("Finally, what is your name, adventurer?")
    while the_name is None:
        the_name = raw_input("\nName: ")
        if not the_name.isalpha():
            the_name = None
            print("Let's try that again. Letters only this time")

    return the_name, the_race, the_class


def game_loop(specs):
    me = Character(*specs)
    inv = Inventory()

    print("\nI hope this turns into something, but who knows?")

    print("Nothing to see here...yet. Move Along!")


def main():
    choice = None
    while choice is None:
        print("""
              Adventure Time
              ==============

              New Game (1)
              Continue (2)
              """)

        print("\nSelection: ")
        choice = raw_input()

    if choice == '1':
        clear()
        game_loop(character_init())

    if choice == '2':
        clear()
        print("Continuing Your Adventure")


if __name__ == "__main__":
    main()
