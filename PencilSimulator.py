

class PencilSimulator():
    def __init__(self, initialDurability=4000):
        self.paper = ''
        self.durability = initialDurability
        self.initialDurability = initialDurability

    def sharpen(self):
        self.durability = self.initialDurability

    def write(self, s):
        for c in s:
            if(self.durability <= 0):
                c = " "
            elif(c >= 'A' and c <= 'Z'):
                self.durability -= 2
            else:
                self.durability -= 1
            self.paper = self.paper + c
        return self.paper
