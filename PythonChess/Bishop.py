from Piece import Piece
from Colors import Colors

class Bishop(Piece):
    def __init__(self, color, place, centralwidget, fullPiecesPath):
        self.movementDirections = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        self.name = "Bishop"
        self.worth = 3

        if color == "white":
            self.icon = "B"
            self.imageLink = fullPiecesPath + "/wB.png"
            print(self.imageLink)
        else:
            self.icon = f"{Colors.BLUE}B{Colors.END}"
            self.imageLink = fullPiecesPath + "/bB.png"
        
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
