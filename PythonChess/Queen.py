from Piece import Piece
from Colors import Colors

class Queen(Piece):
    def __init__(self, color, place):
        Piece.__init__(self, color, place)
        self.movementDirections = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        self.name = "Queen"
        self.worth = 9

        if color == "white":
            self.icon = "Q"
            self.imageLink = "images/pieces/icpieces-png/wQ.png"
        else:
            self.icon = f"{Colors.BLUE}Q{Colors.END}"
            self.imageLink = "images/pieces/icpieces-png/bQ.png"

    def getMovementOptions(self, myBoard):
        movementOptions = []
        viableOptions = []

        for move in self.movementDirections:
            isBlocked = False
            newCoords = self.place

            while self.checkInbounds(newCoords):
                newCoords = (newCoords[0] + move[0], newCoords[1] + move[1])

                if self.checkInbounds(newCoords):
                    if isinstance(myBoard.lookAtSquare(newCoords), Piece):
                        if myBoard.lookAtSquare(newCoords).color != self.color and isBlocked == False:
                            viableOptions.append(newCoords)
                        isBlocked = True

                    if isBlocked == False:
                        viableOptions.append(newCoords)

                    movementOptions.append(newCoords)

        self.movementOptions = movementOptions
        self.viableOptions = viableOptions
