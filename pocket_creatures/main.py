# main.py

from pocket_creatures.save_manager import load_pet, save_pet
from pocket_creatures.game import Game
from pocket_creatures.pet import Pet

def main():
    print("🐾 Welcome to Pocket Creatures")

    pet = load_pet()

    if pet is None:
        print("\nNo save file fouind - let's create a new pet!")
        name = input("What would you like to name your Pocket Creature? ").strip()
        if not name:
            name = "Carl" # if no name is provided
        pet = Pet(name)
        save_pet(pet)
        print(f"\n{name} has been created! Make sure to love him and good care of him!")

    game = Game(pet)
    game.start()

if __name__ == "__main__":
    main()