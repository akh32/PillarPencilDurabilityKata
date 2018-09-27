

class PencilSimulator():
    def __init__(self, initialDurability=4000):
        self.paper = ''
        self.durability = initialDurability

    def write(self, s):
        for c in s:
            if(self.durability == 0):
                c = " "
            else:
                self.durability -= 1
            self.paper = self.paper + c
        return self.paper
