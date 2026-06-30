# save_manager.py
import json
import os
from pocket_creatures.pet import Pet
from pocket_creatures.dragon import Dragon
from pocket_creatures.slime import Slime

SAVE_FILE = "save.json"

def save_pet(pet: Pet):
    data = {
        "name": pet.name,
        "species": getattr(pet, "species", "Pet"),
        "stats": pet.to_dict()
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_pet():
    """Load the pet from disk. Returns a Pet or None if no save exists."""
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    name = data.get("name", "Unknown")
    species = data.get("species", "Pet")
    stats = data.get("stats", {})

    # Reconstruct correct creature type
    if species == "Dragon":
        pet = Dragon(name)
    elif species == "Slime":
        pet = Slime(name)
    else:
        pet = Pet(name)

    # Restore stats

    return pet