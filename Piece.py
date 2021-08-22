class Piece:
    def __init__(self, color, place):
        self.color = color #String
        self.place = place #Tuple (x, y)
        self.movementOptions = set([])
        self.viableOptions = set([])
        self.legalOptions = set([])

    def __repr__(self):
        return self.icon
