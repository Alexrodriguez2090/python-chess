class Piece:
    def __init__(self, color, place):
        self.color = color #String
        self.place = place #Tuple (x, y)
        self.movementOptions = []
        self.viableOptions = []
        self.legalOptions = []

    def __repr__(self):
        return self.icon

    def checkInbounds(self, coords):
        if 0 <= coords[0] <= 7 and 0 <= coords[1] <= 7:
            return True
        else:
            return False
