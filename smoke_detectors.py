SMOKE_THRESHOLD = 50

class SmokeDetector:

    def __init__(self, location, smoke_level):
        self.location = location
        self.smoke_level = smoke_level

    def is_fire(self):
        return self.smoke_level >= SMOKE_THRESHOLD
