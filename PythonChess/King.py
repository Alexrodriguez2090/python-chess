from Piece import Piece
from Colors import Colors

class King(Piece):
    def __init__(self, color, place, centralwidget, fullPiecesPath):
        self.hasMoved = False
        self.movementDirections = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        self.name = "King"

        if color == "white":
            self.icon = "K"
            self.imageLink = fullPiecesPath + "/wK.png"
        else:
            self.icon = f"{Colors.BLUE}K{Colors.END}"
            self.imageLink = fullPiecesPath + "/bK.png"
        
        Piece.__init__(self, color, place, centralwidget)

    def getMovementOptions(self, myBoard): #Fix up king movement
        isBlocked = False
        movementOptions = []
        viableOptions = []

        for move in self.movementDirections:

            newCoords = (self.place[0] + move[0], self.place[1] + move[1])
            if self.checkInbounds(newCoords):
                movementOptions.append(newCoords)

                if isinstance(myBoard.lookAtSquare(newCoords), Piece):
                    if myBoard.lookAtSquare(newCoords).color != self.color:
                        viableOptions.append(newCoords)
                else:
                    viableOptions.append(newCoords)

        self.movementOptions = movementOptions
        self.viableOptions = viableOptions
