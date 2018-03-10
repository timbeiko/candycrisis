class Node: 
    def __init__(self, parent, config, g, h, path): 
        self.parent = parent 
        self.H = h
        self.G = g
        self.F = self.H + self.G 
        self.config = config 
        index = config.index('e')
        self.letter = chr(index + 65)
        self.path = path 

    def __str__(self):
        return "F(n) = " + str(self.F) + "\n" + str(self.config)

    def __repr__(self):
        return "F(n) = " + str(self.F) + "\n" + str(self.config)

    def __eq__(self, other):
         return (self.config == other.config) 