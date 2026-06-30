from pocket_creatures.pet import Pet

class Slime(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Slime"

    def update_stats(self):
        super().update_stats()
        # slimes get dirty and lose happiness quicker
        self.cleanliness = max(0, self.cleanliness - 2)
        self.happiness = max(0, self.happiness - 1)

    def get_mood(self):
        mood = super().get_mood()

        # Slime-specific mode
        if self.cleanliness < 30:
            return "gooey"
        if self.happiness > 30:
            return "bubbly"
        
        return mood