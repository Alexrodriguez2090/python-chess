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

            while 0 <= newCoords[0] <= 7 and 0 <= newCoords[1] <= 7:
                newCoords = (newCoords[0] + move[0], newCoords[1] + move[1])

                if 0 <= newCoords[0] <= 7 and 0 <= newCoords[1] <= 7:
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
        self.viableOptions = viableOptions
