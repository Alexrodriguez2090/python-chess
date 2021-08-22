from Piece import Piece
from Colors import Colors

class King(Piece):
    def __init__(self, color, place):
        Piece.__init__(self, color, place)
        self.hasMoved = False
        self.movementDirections = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        self.name = "King"

        if color == "white":
            self.icon = "K"
        else:
            self.icon = f"{Colors.BLUE}K{Colors.END}"

    def getMovementOptions(self, myBoard):
        isBlocked = False
        movementOptions = set([])
        viableOptions = set([])
        for move in self.movementDirections:
            newCoords = (self.place[0] + move[0], self.place[1] + move[1])
            if newCoords[0] >= 0 and newCoords[0] <= 7 and newCoords[1] >= 0 and newCoords[1] <= 7:
                if isinstance(myBoard.squares[newCoords[0]][newCoords[1]], Piece):

                    if myBoard.squares[newCoords[0]][newCoords[1]].color != self.color:
                        viableOptions.add(newCoords)
                    else:
                        pass
                    isBlocked = True

                if isBlocked == False:
                    viableOptions.add(newCoords)
                movementOptions.add(newCoords)
        self.movementOptions = movementOptions