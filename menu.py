# projects/basic_programs/menu.py

import sys


def load_configuration():
    print("Loading configuration")


def save_configuration():
    print("Saving configuration")


def quit():
    print("Quiting")
    # Optionally really exit the program
    # sys.exit(0)


def what_to_do():
    """Shows a menu and calls the right function based on user input."""
    choice = input("What to do? [load, save, quit]")

    if choice == "load":
        load_configuration()
    elif choice == "save":
        save_configuration()
    elif choice == "quit":
        quit()
    else:
        print("Unknown input")


def main():
    what_to_do()


if __name__ == "__main__":
    main()
