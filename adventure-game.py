#Author- Samson Olowoyo
import time
import random
#might need to do a pip install colorama, if you get an error: ModuleNotFoundError: No module named 'colorama'
from colorama import Fore, Back, Style


def print_sleep(display, delay=2):
    print(display)
    time.sleep(delay)


def game_intro():
    print_sleep(Fore.RED + Back.WHITE + Style.BRIGHT +
                "Welcome to my Adventure game.")
    print_sleep(display="Let the game begin!.", delay=3)
    print_sleep("""
                You are standing in an open field, filled with thorn
                and poison ivy and yellow wildflowers.""")
    print_sleep("""
                Rumor has it that a creature lives somewhere close
                and has been terrorizing the community.""")
    print_sleep("""
                You look scared, but summoned courage from deep within
                to go rid the community of the creature.""")
    print_sleep("""
                Luckily you see a shiny metal on the ground,
                you pick it up to use as a weapon. \n""")
    print_sleep("Let\'s start the game. Be aware of your choices.!!", 5)
    print_sleep("Your choices could impact the community members.")


def lets_play(items):
    pick = ("\n Options 1, 2, 3 only please.!!!!!")
    print_sleep("Enter 1 to knock on the door to get directions.")
    print_sleep("Enter 2 to look inside of the cave.")
    print_sleep("Enter 3 to take a walk around town.")
    action = valid_input("Choose [1|2|3] : ", ['1', '2', '3'])
    if action == '1':
        house(items)
    elif action == '2':
        cave(items)
    elif action == '3':
        town(items)
    else:
        print_sleep(f"Dear Adventurer, Enter Only {pick}")
        lets_play(items)
    play_again(items)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_sleep(f'Sorry, the option "{option}" is invalid. Try again')


def play_again(items):
    choice = valid_input("Play again? [y|n]", ['y', 'n'])
    if choice == 'y':  # option 1 (y)
        print(Style.RESET_ALL)
        play_game()
    else:  # option 2 (n)
        print_sleep('Thanks for playing! Goodbye!')
        print(Style.RESET_ALL)
        exit(0)


def house(items):
    creature = ["cunny fox", "evil monkey", "Liger", "mysterious cat"]
    monster = random.choice(creature)
    print_sleep("You creep towards the door of the house with fear.")
    print_sleep("You knock the door of the house.")
    print_sleep("The door opens and you see a mysterious creature. \n")
    print_sleep("It turns out you knocked on the creature\'s house.")
    print_sleep("Do you want to fight or run away?\n\n")
    print_sleep("Enter 1 to fight, 2 to run away.")
    response = valid_input('[1. fight |2. run] :', ['1', '2'])
    if response == "1" and "sword" in items:
        print(f"You need a powerful weapon to defeat the {monster}.")
        print_sleep(f"The sees a shiny sword in your hand, \n"
                    "and runs away, as he\'s no match for such weapon.", 3)
        print_sleep(f"You defeated the {monster} and win the game.")
    elif response == "1" and "mighty potion" in items:
        print(f"You need a powerful weapon to defeat the {monster}.")
        print_sleep(f"The {monster} sees a shiny blunt metal, laughs \n"
                    "but he\'s no match for the potion you took earlier.", 3)
        print_sleep(f"You defeated the {monster} and win the game.")
    elif response == "1" and "sword" and "mighty potion" in items:
        print_sleep("Bring your best game monster!!! I'm fully loaded.")
        print_sleep(f"You cut the {monster} into pieces and won.")
        print_sleep(f"You defeated the {monster} and win the game.")
    elif response == "2":
        print_sleep("It\'s a good day to run away from the enemy.", 1)
    else:
        print_sleep(f"You need a powerful weapon to defeat the {monster}.")
        print_sleep("You are defeated, you lost the game.", 3)
        return monster


def cave(items):
    print_sleep("You look inside the dark cave")
    print_sleep("Lying on a piece of rock, you see an ancient shiny sword.", 1)
    print_sleep("Will you pick up the sword? Yes/No")
    choice = valid_input("Play again? [y|n]", ['y', 'n'])
    if choice == 'y':
        print_sleep("You have the sword of Zoro.", 1)
        items.append("sword")
        lets_play(items)
    else:
        print_sleep("What do you want to do next?", 1)
        lets_play(items)


def town(items):
    print_sleep("You decided to take a stroll around the community, \n"
                "because you feel under-prepared to face the creature.")
    print_sleep("You see a red door house with a door signpost that \n"
                "says 'WELCOME GREAT WARRIOR'.")
    print_sleep("Do you want to enter or walk away ? Y/N")
    choice = valid_input("Play again? [y|n]", ['y', 'n'])
    if choice == 'y':
        items.append("mighty potion")
        print_sleep("You enter the house and you see an historian \n"
                    "he tells you a tale of the town and the creature.")
        print_sleep("You feel so energized and confident now.", 1)
        print_sleep("Ready to face the creature?", 3)
        lets_play(items)
    else:
        print_sleep("Continue your fun adventure.")
        lets_play(items)


def play_game():
    items = []
    game_intro()
    lets_play(items)


play_game()
