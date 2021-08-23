from Piece import Piece
from Colors import Colors

class Rook(Piece):
    def __init__(self, color, place):
        Piece.__init__(self, color, place)
        self.hasMoved = False
        self.movementDirections = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.name = "Rook"

        if color == "white":
            self.icon = "R"
        else:
            self.icon = f"{Colors.BLUE}R{Colors.END}"

    def getMovementOptions(self, myBoard):
        movementOptions = set([])
        viableOptions = set([])

        for move in self.movementDirections:
            isBlocked = False
            newCoords = self.place

            while self.checkInbounds(newCoords):
                newCoords = (newCoords[0] + move[0], newCoords[1] + move[1])

                if self.checkInbounds(newCoords):
                    if isinstance(myBoard.lookAtSquare(newCoords), Piece):
                        if myBoard.lookAtSquare(newCoords).color != self.color and isBlocked == False:
                            viableOptions.add(newCoords)
                        isBlocked = True

                    if isBlocked == False:
                        viableOptions.add(newCoords)

                    movementOptions.add(newCoords)

        self.movementOptions = movementOptions
        self.viableOptions = viableOptions
