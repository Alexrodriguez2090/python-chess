from Piece import Piece
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from King import King
from Pawn import Pawn
import copy

def getListOfAllPieces(myBoard):
    allPieces = []
    for row in myBoard.squares:
        for square in row:
            if isinstance(square, Piece):
                allPieces.append(square)
    return allPieces

def getAllMovementOptions(myBoard, allPieces):
    for piece in allPieces:
        piece.getMovementOptions(myBoard)

def updateMovementOptions(squareMovedFrom, squareMovedTo, myBoard):
    allPieces = parseThroughBoard(myBoard)

    for piece in allPieces:
        if squareMovedFrom in myBoard.lookAtSquare(piece[2]).movementDirections or squareMovedTo in myBoard.lookAtSquare(piece[2]).movementDirections:
            myBoard.lookAtSquare(piece[2]).getMovementOptions(myBoard)

def getAllyKingPiece(allPieces, colorPlaying):
    for piece in allPieces:
        if isinstance(piece, King) and piece.color == colorPlaying:
            return piece

def getOppKingPiece(allPieces, colorPlaying):
    for piece in allPieces:
        if isinstance(piece, King) and piece.color != colorPlaying:
            return piece

def _getLegalMoves(testBoard, myMove, piece, colorPlaying, king, oppKing):
    squareMovedTo = testBoard.squares[myMove[0]][myMove[1]]
    testBoard.squares[myMove[0]][myMove[1]] = testBoard.lookAtSquare(piece.place)
    testBoard.squares[piece.place[0]][piece.place[1]] = 0

    rookMoves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    bishopMoves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    knightMoves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    if colorPlaying == "white":
        pawnMoves = [(1, 1), (1, -1)]
    elif colorPlaying == "black":
        pawnMoves = [(-1, 1), (-1, -1)]

    for move in bishopMoves:
        foundPiece = False
        kingVision = (king.place[0] + move[0], king.place[1] + move[1])
        while king.checkInbounds(kingVision) and foundPiece == False:
            if isinstance(testBoard.lookAtSquare(kingVision), Piece):
                foundPiece = True
                if isinstance(testBoard.lookAtSquare(kingVision), Bishop) or isinstance(testBoard.lookAtSquare(kingVision), Queen):
                    if colorPlaying != testBoard.lookAtSquare(kingVision).color:
                        return
            else:
                kingVision = (kingVision[0] + move[0], kingVision[1] + move[1])

    for move in knightMoves:
        kingSquare = king.place
        if king.checkInbounds(kingSquare):
            if isinstance(testBoard.lookAtSquare(kingSquare), Knight):
                if colorPlaying != testBoard.lookAtSquare(kingSquare).color:
                    return

    for move in rookMoves:
        foundPiece = False
        kingVision = (king.place[0] + move[0], king.place[1] + move[1])

        while king.checkInbounds(kingVision) and foundPiece == False:
            if isinstance(testBoard.lookAtSquare(kingVision), Piece):
                foundPiece = True
                if isinstance(testBoard.lookAtSquare(kingVision), Rook) or isinstance(testBoard.lookAtSquare(kingVision), Queen):
                    if colorPlaying != testBoard.lookAtSquare(kingVision).color:
                        return
            else:
                kingVision = (kingVision[0] + move[0], kingVision[1] + move[1])

    for move in pawnMoves:
        kingSquare = king.place
        if king.checkInbounds(kingSquare):
            if isinstance(testBoard.lookAtSquare(kingSquare), Pawn):
                if colorPlaying != testBoard.lookAtSquare(kingSquare).color:
                    return

    piece.legalOptions.append(myMove)

def getLegalMoves(myBoard, colorPlaying):
    allPieces = getListOfAllPieces(myBoard)
    getAllMovementOptions(myBoard, allPieces)

    king = getAllyKingPiece(allPieces, colorPlaying)
    oppKing = getOppKingPiece(allPieces, colorPlaying)
    testBoard = copy.deepcopy(myBoard)

    for piece in allPieces:
        if piece.color == colorPlaying:
            piece.legalOptions = []
            for myMove in piece.viableOptions:
                squareMovedTo = testBoard.squares[myMove[0]][myMove[1]] #Save the piece being moved into
                _getLegalMoves(testBoard, myMove, piece, colorPlaying, king, oppKing)

                #Put the pieces back
                testBoard.squares[piece.place[0]][piece.place[1]] = testBoard.squares[myMove[0]][myMove[1]]
                testBoard.squares[myMove[0]][myMove[1]] = squareMovedTo

    for oppMove in oppKing.movementOptions:
        if oppMove in king.legalOptions:
            king.legalOptions.remove(oppMove)

def movePiece(myBoard, pieceMoved, squareMovedTo, colorPlaying): #cleanup after actually working
    if isinstance(myBoard.lookAtSquare(pieceMoved), Piece):
        if squareMovedTo in myBoard.lookAtSquare(pieceMoved).legalOptions and colorPlaying == myBoard.lookAtSquare(pieceMoved).color:
            myBoard.squares[squareMovedTo[0]][squareMovedTo[1]] = myBoard.squares[pieceMoved[0]][pieceMoved[1]]
            myBoard.squares[pieceMoved[0]][pieceMoved[1]] = 0
            return True

    else:
        return False
