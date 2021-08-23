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

        oneForward = (self.place[0] + self.movementDirections[0][0], self.place[1] + self.movementDirections[0][1])
        if self.checkInbounds(oneForward):
            movementOptions.add(oneForward)
            if not isinstance(myBoard.lookAtSquare(oneForward), Piece):
                viableOptions.add(oneForward)

        if self.hasMoved == False:
            twoForward = (oneForward[0] + self.movementDirections[0][0], oneForward[1] + self.movementDirections[0][1])
            if self.checkInbounds(twoForward):
                movementOptions.add(twoForward)
                if not isinstance(myBoard.lookAtSquare(twoForward), Piece) and not isinstance(myBoard.lookAtSquare(oneForward), Piece):
                    viableOptions.add(twoForward)

        for attackDirection in self.attackDirections:
            attackedCoord = (self.place[0] + attackDirection[0], self.place[1] + attackDirection[1])
            if self.checkInbounds(attackedCoord):
                movementOptions.add(attackedCoord)
                if isinstance(myBoard.lookAtSquare(attackedCoord), Piece):
                    if myBoard.lookAtSquare(attackedCoord).color != self.color:
                        viableOptions.add(attackedCoord)

        self.movementOptions = movementOptions
        self.viableOptions = viableOptions
