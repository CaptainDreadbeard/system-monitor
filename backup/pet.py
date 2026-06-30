# pet.py
import time

class Pet:
    def __init__(self, name, hunger=50, energy=50, happiness=50, cleanliness=50, last_update=None):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.cleanliness = cleanliness
        self.last_update = last_update or time.time()

    # ------------------------------------------------
    # Internal Helpers
    # ------------------------------------------------

    def _clamp(self, value):
        return max(0, min(100, value))
    
    def _apply_decay(self):
        """Decay stats based on time passed since last update."""
        now = time.time()
        elapsed = now - self.last_update #seconds

        # Decay rates per second
        hunger_decay = 0.01
        energy_decay = 0.008
        happiness_decay = 0.006
        cleanliness_decay = 0.004

        self.hunger = self._clamp(self.hunger - hunger_decay * elapsed)
        self.energy = self._clamp(self.energy - energy_decay * elapsed)
        self.happiness = self._clamp(self.happiness - happiness_decay * elapsed)
        self.cleanliness = self._clamp(self.cleanliness - cleanliness_decay * elapsed)

        self.last_update = now

    # ------------------------------------------------
    # Public methods 
    # ------------------------------------------------
    def update_stats(self):
        self._apply_decay()

    def feed(self):
        self.update_stats()
        self.hunger = self._clamp(self.hunger + 25)
        self.cleanliness = self._clamp(self.cleanliness - 5)

    def play(self):
        self.update_stats()
        self.happiness = self._clamp(self.happiness + 20)
        self.energy = self._clamp(self.energy - 10)
        self.hunger = self._clamp(self.hunger - 5)

    def sleep(self):
        self.update_stats()
        self.energy = self._clamp(self.energy + 30)
        self.hunger = self._clamp(self.hunger - 10)

    def clean(self):
        self.update_stats()
        self.cleanliness = self._clamp(self.cleanliness + 30)
        self.happiness = self._clamp(self.happiness + 5)

    # ------------------------------------------------
    # Mood Logic
    # ------------------------------------------------
    def get_mood(self):
        """Return a mood string based on the pets current stats"""
        stats = {
            "hunger": self.hunger,
            "energy": self.energy,
            "happiness": self.happiness
        }

        # Priority moods
        if self.hunger < 20:
            return "hungry"
        if self.energy < 20:
            return "tired"
        if self.happiness < 20:
            return "sad"
        
        # Good moods
        if all(v > 70 for v in stats.values()):
            return "ecstatic"
        if all(v > 50 for v in stats.values()):
            return "happy"
        
        return "neutral"
    
    # -------------------------------------------------
    # Serialization
    # -------------------------------------------------
    def to_dict(self):
        return {
            "name": self.name,
            "hunger": self.hunger,
            "energy": self.energy,
            "happiness": self.happiness,
            "cleanliness": self.cleanliness,
            "last_update": self.last_update
        }

    @staticmethod
    def from_dict(data):
        return Pet(
            name=data["name"],
            hunger=data["hunger"],
            energy=data["energy"],
            happiness=data["happiness"],
            cleanliness=data["cleanliness"],
            last_update=data["last_update"]
        )