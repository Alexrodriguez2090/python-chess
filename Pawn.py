from Piece import Piece
from Colors import Colors

class Pawn(Piece):
    def __init__(self, color, place):
        Piece.__init__(self, color, place)
        self.hasMoved = False
        self.justMovedTwoSquares = False
        self.name = "Pawn"

        if self.color == "white":
            self.movementDirections = [(-1, 0)]
            self.attackDirections = [(-1, 1), (-1, -1)]
            self.icon = "P"
        elif self.color == "black":
            self.movementDirections = [(1, 0)]
            self.attackDirections = [(1, 1), (1, -1)]
            self.icon = f"{Colors.BLUE}P{Colors.END}"

    def getMovementOptions(self, myBoard):
        movementOptions = set([])
        viableOptions = set([])

        newCoords = (self.place[0] + self.movementDirections[0][0], self.place[1] + self.movementDirections[0][1])
        if newCoords[0] >= 0 and newCoords[0] <= 7 and newCoords[1] >= 0 and newCoords[1] <= 7:
            movementOptions.add(newCoords)
            if not isinstance(myBoard.lookAtSquare(newCoords), Piece):
                viableOptions.add(newCoords)

        if self.hasMoved == False:
            twoForward = (newCoords[0] + self.movementDirections[0][0], newCoords[1] + self.movementDirections[0][1])
            movementOptions.add(newCoords)
            if not isinstance(myBoard.lookAtSquare(twoForward), Piece):
                viableOptions.add(newCoords)

        self.movementOptions = movementOptions
        self.viableOptions = viableOptions
