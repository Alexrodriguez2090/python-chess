from Piece import Piece
from Colors import Colors

class Bishop(Piece):
    def __init__(self, color, place):
        Piece.__init__(self, color, place)
        self.movementDirections = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        self.name = "Bishop"

        if color == "white":
            self.icon = "B"
        else:
            self.icon = f"{Colors.BLUE}B{Colors.END}"

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

                        if myBoard.lookAtSquare(newCoords).color != self.color:
                            viableOptions.add(newCoords)
                        else:
                            pass
                        isBlocked = True

                    if isBlocked == False:
                        viableOptions.add(newCoords)

                    movementOptions.add(newCoords)

        self.movementOptions = movementOptions
        self.viableOptions = viableOptions
