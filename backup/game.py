# game.py

import random
import time
from pocket_creatures.ascii_art import get_art
from pocket_creatures.save_manager import save_pet
from pocket_creatures.pet import Pet

COMMANDS = ["feed", "play", "sleep", "clean", "stats", "help", "quit"]


def stat_bar(value, length=12):
    """Return a visual bar for a stat (0–100)."""
    filled = int((value / 100) * length)
    empty = length - filled
    return "█" * filled + "░" * empty


class Game:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.running = True

    # -----------------------------
    # Rendering
    # -----------------------------
    def render(self):
        self.pet.update_stats()
        mood = self.pet.get_mood()
        art = get_art(mood, getattr(self.pet, "species", "Pet"))

        print("\n" + "=" * 40)
        print(f"{self.pet.name}'s Current Mood: {mood.upper()}")
        print(art)
        print("=" * 40)

    def show_stats(self):
        print(f"""
Stats for {self.pet.name}:
--------------------------
Hunger:       {stat_bar(self.pet.hunger)}  {self.pet.hunger:.1f}
Energy:       {stat_bar(self.pet.energy)}  {self.pet.energy:.1f}
Happiness:    {stat_bar(self.pet.happiness)}  {self.pet.happiness:.1f}
Cleanliness:  {stat_bar(self.pet.cleanliness)}  {self.pet.cleanliness:.1f}
""")

    # -----------------------------
    # Random Events
    # -----------------------------
    def random_event(self):
        if random.random() < 0.15:  # 15% chance per action
            event = random.choice([
                ("found a gold coin!", +5),
                ("took a cute nap!", +10),
                ("got scared by a drive-by!", -10),
                ("ate a gyro!", +8),
                ("stepped in poop!", -8)
            ])
            message, happiness_change = event
            self.pet.happiness = max(0, min(100, self.pet.happiness + happiness_change))
            print(f"\n✨ Random Event: Your pet {message} (Happiness {happiness_change:+})")

    # -----------------------------
    # Command Handling
    # -----------------------------
    def handle_command(self, cmd):
        cmd = cmd.lower().strip()

        if cmd == "feed":
            self.pet.feed()
            print("🍎 Thanks for feeding me!")
        elif cmd == "play":
            self.pet.play()
            print("🎾 Thanks for playing with me!")
        elif cmd == "sleep":
            self.pet.sleep()
            print("💤 Your pet took a nap!")
        elif cmd == "clean":
            self.pet.clean()
            print("🧼 Thanks for cleaning me!")
        elif cmd == "stats":
            self.show_stats()
        elif cmd == "help":
            print("Available commands:", ", ".join(COMMANDS))
        elif cmd == "quit":
            print("Saving and exiting...")
            save_pet(self.pet)
            self.running = False
            return
        else:
            print("Unknown command. Type 'help' for options.")

        # After every action:
        save_pet(self.pet)
        self.random_event()

    # -----------------------------
    # Main Loop
    # -----------------------------
    def start(self):
        print(f"\nWelcome back, {self.pet.name}!")
        print("Type 'help' for a list of commands.\n")

        while self.running:
            self.render()
            cmd = input("What would you like to do? > ")
            self.handle_command(cmd)
            time.sleep(0.3)
