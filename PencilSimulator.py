

class PencilSimulator():
    def __init__(self, initialDurability=4000, length = 2):
        self.paper = ''
        self.durability = initialDurability
        self.initialDurability = initialDurability
        self.length = length

    def sharpen(self):
        if(self.length > 0):
            self.durability = self.initialDurability
            self.length -= 1

    def erase(self, s):
        i = self.paper.find(s)
        if(i > -1):
            self.paper = self.paper[0:i] + " "*len(s) + self.paper[i+len(s):]
        return self.paper

    def write(self, s):
        for c in s:
            if(self.durability <= 0):
                c = " "
            elif(c == " " or c == "\n"):
                self.durability = self.durability
            elif(c >= 'A' and c <= 'Z'):
                self.durability -= 2
            else:
                self.durability -= 1
            self.paper = self.paper + c
        return self.paper
