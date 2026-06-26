# save_manager.py
import json
import os
from pocket_creatures.pet import Pet

SAVE_FILE = "save.json"

def save_pet(pet: Pet):
 """Save the pets state to a JSON file."""
 data = pet.to_dict()
 with open(SAVE_FILE, "w") as f:
   json.dump(data, f, indent=4)

def load_pet():
    """Load the pet from disk. Returns a Pet or None if no save exists."""
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    return Pet.from_dict(data)