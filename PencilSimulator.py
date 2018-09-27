

class PencilSimulator():
    def __init__(self):
        self.paper = ''
        
    def write(self, s):
        self.paper = self.paper + s
        return self.paper
