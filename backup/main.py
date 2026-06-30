# main.py

from pocket_creatures.save_manager import load_pet, save_pet
from pocket_creatures.game import Game
from pocket_creatures.pet import Pet
from pocket_creatures.dragon import Dragon
from pocket_creatures.slime import Slime

def main():
    print("🐾 Welcome to Pocket Creatures")
    # Load existing pet
    pet = load_pet()

    if pet is None:
        print("\nNo Save File found - let's create a creature!")
    
        name = input("What would you like to name your creature?: ").strip()
        if not name:
            name = "Carl"

        print("Choose your creature type:")
        print("1. Bunny")
        print("2. Dragon")
        print("3. Slime")

        choice = input("Enter your pets number here: ").strip()

        if choice == "2":
            pet = Dragon(name)
        elif choice == "3":
            pet = Slime(name)
        else:
            pet = Pet(name)

        save_pet(pet)
        
        print(f"\n{name} has been created! TAKE GOOD CARE OF THEM")
    
    # Start the game
    game = Game(pet)
    game.start()

if __name__ == "__main__":
    main()