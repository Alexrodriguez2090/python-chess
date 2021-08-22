from Piece import Piece
from Pawn import Pawn

def parseThroughBoard(myBoard):
    #[["color", "piecetype", (row, column)]]
    #piece[0] is color
    #piece[1] is piecetype
    #piece[2] is tuple (row, column)
    #piece[2][0] is row
    #piece[2][1] is column
    allPieces = []
    for row in range(8):
        for column in range(8):
            if isinstance(myBoard.lookAtSquare((row, column)), Piece):
                allPieces.append([myBoard.lookAtSquare((row, column)).color, myBoard.lookAtSquare((row, column)).name, (row, column)])
    return allPieces

def getAllMovementOptions(myBoard):
    allPieces = parseThroughBoard(myBoard)

    for piece in allPieces:
        myBoard.lookAtSquare(piece[2]).getMovementOptions(myBoard)

def updateMovementOptions(squareMovedFrom, squareMovedTo, myBoard):
    allPieces = parseThroughBoard(myBoard)

    for piece in allPieces:
        if squareMovedFrom in myBoard.lookAtSquare(piece[2]).movementDirections or squareMovedTo in myBoard.lookAtSquare(piece[2]).movementDirections:
            myBoard.lookAtSquare(piece[2]).getMovementOptions(myBoard)

def checkPawnAttack(pawn, myBoard, allPieces): #Rewrite to pawn class
    for piece in allPieces:
        for attackDirection in pawn.attackDirections:
            attackedCoord = (pawn.place[0] + direction[0], pawn.place[1] + direction[1])
            if attackedCoord == piece[2]:
                pawn.viableOptions.add(attackedCoord)

def checkForChecks(piece, oppKing):
    if oppKing.place in piece.viableOptions:
        return True
    else:
        return False

def checkForPins(piece, myBoard, oppKing):
    #If 'piece' has a line at the king, but there's at least one other piece in the middle
    if oppKing.place in piece.movementOptions and oppKing.place not in piece.viableOptions:
        moveLength = (oppKing.place[0] - piece.place[0], oppKing.place[1] - piece.place[1])

        #Gets movement direction of piece toward the king
        moveDirection = ()
        for coord in moveLength:
            if coord > 0:
                moveDirection += (1,)
            elif coord < 0:
                moveDirection += (-1,)
            elif coord == 0:
                moveDirection += (0,)

        #Looks at which squares there are between the piece and the king
        movement = (piece.place[0] + moveDirection[0], piece.place[1] + moveDirection[1])
        pieceLookingThrough = []
        while movement != oppKing.place:
            pieceLookingThrough.append(movement)
            movement = (movement[0] + moveDirection[0], movement[1] + moveDirection[1])

        #If it's greater than one square, it means there could or could not be more than one piece
        semiPinnedPieces = []
        if len(pieceLookingThrough) > 1:
            for square in pieceLookingThrough:
                if isinstance(myBoard.lookAtSquare((row, column)), Piece):
                    semiPinnedPieces.append((row, column))
                if len(semiPinnedPieces) > 1: #If there is more than one piece, we do not have a pin
                    return False
        else: #Else there is only one square between the king and the piece, meaning it has to be pinned if it is opposite color
            semiPinnedPieces = pieceLookingThrough

        #If the one piece in the middle is a different color, it is pinned
        if piece.color != myBoard.lookAtSquare(pieceLookingThrough[0]).color:
            return pieceLookingThrough[0]
        else: #If the piece in the middle is the same color
            return False

    else:
        return False

def getLegalMoves(myBoard):
    allPieces = parseThroughBoard(myBoard)

    for piece in allPieces:
        if piece[1] == "Pawn":
            pass
        elif piece[1] != "King":
            pass
        elif piece[1] == "King":
            pass


def checkForPinsBad(myBoard): #Rewrite for piece by piece usage
    allPieces = parseThroughBoard(myBoard)

    kings = []
    for piece in allPieces:
        if piece.name == "King":
            kings.append(piece)
            if len(kings) == 2:
                break

    for king in kings:
        for piece in allPieces:
            if king[2] in myBoard.lookAtSquare(piece[2]).movementOptions and king[2] not in myBoard.lookAtSquare(piece[2]).viableOptions: #If another piece is directly looking at a king, but there's at least one piece in the middle
                if myBoard.lookAtSquare(piece[2]).color != king[0]: #If that piece is opposite color
                    moveLength = (king[2][0] - piece[2][0], king[2][1] - piece[2][1])

                    moveDirection = ()
                    for coord in moveLength:
                        if coord > 0:
                            moveDirection += (1,)
                        elif coord < 0:
                            moveDirection += (-1,)
                        elif coord == 0:
                            moveDirection += (0,)

                    movement = (piece[2][0] + moveDirection[0], piece[2][1] + moveDirection[1])
                    pieceLookingThrough = []
                    while movement != king[2]:
                        pieceLookingThrough.append(movement)
                        movement = (movement[0] + moveDirection[0], movement[1] + moveDirection[1])

                    if len(pieceLookingThrough) > 1:
                        semiPinnedPieces = []
                        for square in pieceLookingThrough:
                            if isinstance(myBoard.lookAtSquare((row, column)), Piece):
                                semiPinnedPieces.append((row, column))
                            if len(semiPinnedPieces) > 1:
                                return False
                    else: #Else there is only one piece being pinned
                        return

                    if len(semiPinnedPieces) > 1:
                        pass
            else:
                return False
def checkForChecksBad(myBoard): #Only allow legal moves that get the king out of check, can be a pin
    allPieces = parseThroughBoard(myBoard)

    kings = []
    for piece in allPieces:
        if piece.name == "King":
            kings.append(piece)
            if len(kings) == 2:
                break

    for king in kings:
        for piece in allPieces:
            if king[2] in myBoard.lookAtSquare(piece[2]).viableOptions: #If another piece is directly looking at a king
                if myBoard.lookAtSquare(piece[2]).color != king[0]: #If that piece is opposite color
                    if king[0] == "white":
                        return 0
                    if king[0] == "black":
                        return 1
    return False
