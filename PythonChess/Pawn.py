from Piece import Piece
from Colors import Colors

class Pawn(Piece):
    def __init__(self, color, place):
        Piece.__init__(self, color, place)
        self.hasMoved = False
        self.justMovedTwoSquares = False
        self.name = "Pawn"
        self.worth = 1

        if self.color == "white":
            self.movementDirections = [(-1, 0)]
            self.attackDirections = [(-1, 1), (-1, -1)]
            self.icon = "P"
            self.imageLink = "images/pieces/icpieces-png/wP.png"
        else:
            self.movementDirections = [(1, 0)]
            self.attackDirections = [(1, 1), (1, -1)]
            self.icon = f"{Colors.BLUE}P{Colors.END}"
            self.imageLink = "images/pieces/icpieces-png/bP.png"

    def getMovementOptions(self, myBoard):
        movementOptions = []
        viableOptions = []

        oneForward = (self.place[0] + self.movementDirections[0][0], self.place[1] + self.movementDirections[0][1])
        if self.checkInbounds(oneForward):
            movementOptions.append(oneForward)
            if not isinstance(myBoard.lookAtSquare(oneForward), Piece):
                viableOptions.append(oneForward)

        if self.hasMoved == False:
            twoForward = (oneForward[0] + self.movementDirections[0][0], oneForward[1] + self.movementDirections[0][1])
            if self.checkInbounds(twoForward):
                movementOptions.append(twoForward)
                if not isinstance(myBoard.lookAtSquare(twoForward), Piece) and not isinstance(myBoard.lookAtSquare(oneForward), Piece):
                    viableOptions.append(twoForward)

        for attackDirection in self.attackDirections:
            attackedCoord = (self.place[0] + attackDirection[0], self.place[1] + attackDirection[1])
            if self.checkInbounds(attackedCoord):
                movementOptions.append(attackedCoord)
                if isinstance(myBoard.lookAtSquare(attackedCoord), Piece):
                    if myBoard.lookAtSquare(attackedCoord).color != self.color:
                        viableOptions.append(attackedCoord)

        self.movementOptions = movementOptions
        self.viableOptions = viableOptions
