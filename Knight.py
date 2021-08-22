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
        movementOptions = set([])
        viableOptions = set([])

        for move in self.movementDirections:
            newCoords = (self.place[0] + move[0], self.place[1] + move[1])
            if 0 <= newCoords[0] <= 7 and 0 <= newCoords[1] <= 7:
                if isinstance(myBoard.squares[newCoords[0]][newCoords[1]], Piece): #If there is another piece on the square
                    if myBoard.squares[newCoords[0]][newCoords[1]].color != self.color:
                        viableOptions.add(newCoords)
                    else:
                        pass

                else:
                    viableOptions.add(newCoords)
                movementOptions.add(newCoords)

        self.movementOptions = movementOptions
        self.viableOptions = viableOptions
