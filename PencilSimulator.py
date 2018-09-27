

class PencilSimulator():
    def __init__(self, initialDurability=4000):
        self.paper = ''
        self.durability = initialDurability

    def write(self, s):
        if(self.durability == 0):
            self.paper = self.paper + " " * len(s)
            return self.paper
        self.paper = self.paper + s
        return self.paper
