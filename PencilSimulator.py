

class PencilSimulator():
    def __init__(self, initialDurability=4000, length = 2, eraserDurability = 1000):
        self.paper = ''
        self.durability = initialDurability
        self.initialDurability = initialDurability
        self.length = length
        self.eraser = eraserDurability

    def sharpen(self):
        if(self.length > 0):
            self.durability = self.initialDurability
            self.length -= 1

    def erase(self, s):
        i = self.paper.rfind(s)
        if(i > -1):
            j = max(0, len(s) - self.eraser)
            self.paper = self.paper[0:i+j] + " "*(len(s)-j) + self.paper[i+len(s):]
            self.eraser = max(0, self.eraser - len(s))
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
