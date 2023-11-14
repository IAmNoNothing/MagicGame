class Wand:
    def __init__(self, stats):
        self.stats = stats
        self.spells = []

    def cast(self):
        for spell in self.spells:
            spell.cast()
