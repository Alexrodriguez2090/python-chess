from Piece import Piece
from Colors import Colors

class Rook(Piece):
    def __init__(self, color, place, centralwidget, fullPiecesPath):
        self.hasMoved = False
        self.movementDirections = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.name = "Rook"
        self.worth = 5

        if color == "white":
            self.icon = "R"
            self.imageLink = fullPiecesPath + "/wR.png"
        else:
            self.icon = f"{Colors.BLUE}R{Colors.END}"
            self.imageLink = fullPiecesPath + "/bR.png"
        
        Piece.__init__(self, color, place, centralwidget)

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
