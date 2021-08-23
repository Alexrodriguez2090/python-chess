from Piece import Piece
from Colors import Colors

class Knight(Piece):
    def __init__(self, color, place):
        Piece.__init__(self, color, place)
        self.movementDirections = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        self.name = "Knight"

        if color == "white":
            self.icon = "N"
        else:
            self.icon = f"{Colors.BLUE}N{Colors.END}"

    def getMovementOptions(self, myBoard):
        movementOptions = []
        viableOptions = []

        for move in self.movementDirections:
            newCoords = (self.place[0] + move[0], self.place[1] + move[1])
            if self.checkInbounds(newCoords):
                if isinstance(myBoard.lookAtSquare(newCoords), Piece): #If there is another piece on the square
                    if myBoard.lookAtSquare(newCoords).color != self.color:
                        viableOptions.append(newCoords)
                    else:
                        pass

                else:
                    viableOptions.append(newCoords)
                movementOptions.append(newCoords)

        self.movementOptions = movementOptions
        self.viableOptions = viableOptions
