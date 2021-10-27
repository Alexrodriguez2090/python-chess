from Piece import Piece
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from King import King
from Pawn import Pawn
import copy

class MoveEngine():
    def __init__(self):
        self.colorPlaying = None
        self.allPieces = []

    def getListOfAllPieces(self, myBoard):
        self.allPieces = []
        for row in myBoard.squares:
            for square in row:
                if isinstance(square, Piece):
                    self.allPieces.append(square)

    def getAllMovementOptions(self, myBoard):
        for piece in self.allPieces:
            piece.getMovementOptions(myBoard)

    def updateMovementOptions(self, squareMovedFrom, squareMovedTo, myBoard):
        self.allPieces = parseThroughBoard(myBoard)

        for piece in self.allPieces:
            if squareMovedFrom in myBoard.lookAtSquare(piece[2]).movementDirections or squareMovedTo in myBoard.lookAtSquare(piece[2]).movementDirections:
                myBoard.lookAtSquare(piece[2]).getMovementOptions(myBoard)

    def getAllyKingPiece(self):
        for piece in self.allPieces:
            if isinstance(piece, King) and piece.color == self.colorPlaying:
                return piece

    def getOppKingPiece(self):
        for piece in self.allPieces:
            if isinstance(piece, King) and piece.color != self.colorPlaying:
                return piece

    def getColorPlaying(self):
        if self.colorPlaying == "white":
            self.colorPlaying = "black"
        elif self.colorPlaying == "black":
            self.colorPlaying = "white"
        elif self.colorPlaying == None:
            self.colorPlaying = "white"

    def _getLegalMoves(self, testBoard, myMove, piece, king, oppKing):
        squareMovedTo = testBoard.squares[myMove[0]][myMove[1]]
        testBoard.squares[myMove[0]][myMove[1]] = testBoard.lookAtSquare(piece.place)
        testBoard.squares[piece.place[0]][piece.place[1]] = 0

        rookMoves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        bishopMoves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        knightMoves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        if self.colorPlaying == "white":
            pawnMoves = [(1, 1), (1, -1)]
        elif self.colorPlaying == "black":
            pawnMoves = [(-1, 1), (-1, -1)]

        for move in bishopMoves:
            foundPiece = False
            kingVision = (king.place[0] + move[0], king.place[1] + move[1])
            while king.checkInbounds(kingVision) and foundPiece == False:
                if isinstance(testBoard.lookAtSquare(kingVision), Piece):
                    foundPiece = True
                    if isinstance(testBoard.lookAtSquare(kingVision), Bishop) or isinstance(testBoard.lookAtSquare(kingVision), Queen):
                        if self.colorPlaying != testBoard.lookAtSquare(kingVision).color:
                            return
                else:
                    kingVision = (kingVision[0] + move[0], kingVision[1] + move[1])

        for move in knightMoves:
            kingSquare = king.place
            if king.checkInbounds(kingSquare):
                if isinstance(testBoard.lookAtSquare(kingSquare), Knight):
                    if self.colorPlaying != testBoard.lookAtSquare(kingSquare).color:
                        return

        for move in rookMoves:
            foundPiece = False
            kingVision = (king.place[0] + move[0], king.place[1] + move[1])

            while king.checkInbounds(kingVision) and foundPiece == False:
                if isinstance(testBoard.lookAtSquare(kingVision), Piece):
                    foundPiece = True
                    if isinstance(testBoard.lookAtSquare(kingVision), Rook) or isinstance(testBoard.lookAtSquare(kingVision), Queen):
                        if self.colorPlaying != testBoard.lookAtSquare(kingVision).color:
                            return
                else:
                    kingVision = (kingVision[0] + move[0], kingVision[1] + move[1])

        for move in pawnMoves:
            kingSquare = king.place
            if king.checkInbounds(kingSquare):
                if isinstance(testBoard.lookAtSquare(kingSquare), Pawn):
                    if self.colorPlaying != testBoard.lookAtSquare(kingSquare).color:
                        return

        piece.legalOptions.append(myMove)

    def getLegalMoves(self, myBoard):
        self.getListOfAllPieces(myBoard)
        self.getAllMovementOptions(myBoard)

        king = self.getAllyKingPiece()
        oppKing = self.getOppKingPiece()
        testBoard = copy.deepcopy(myBoard)

        for piece in self.allPieces:
            if piece.color == self.colorPlaying:
                piece.legalOptions = []
                for myMove in piece.viableOptions:
                    squareMovedTo = testBoard.squares[myMove[0]][myMove[1]] #Save the piece being moved into
                    self._getLegalMoves(testBoard, myMove, piece, king, oppKing)

                    #Put the pieces back
                    testBoard.squares[piece.place[0]][piece.place[1]] = testBoard.squares[myMove[0]][myMove[1]]
                    testBoard.squares[myMove[0]][myMove[1]] = squareMovedTo

        for oppMove in oppKing.movementOptions:
            if oppMove in king.legalOptions:
                king.legalOptions.remove(oppMove)

    def movePiece(self, myBoard, pieceMoved, squareMovedTo): #cleanup after actually working
        if isinstance(myBoard.lookAtSquare(pieceMoved), Piece):
            if squareMovedTo in myBoard.lookAtSquare(pieceMoved).legalOptions and self.colorPlaying == myBoard.lookAtSquare(pieceMoved).color:
                myBoard.squares[squareMovedTo[0]][squareMovedTo[1]] = myBoard.squares[pieceMoved[0]][pieceMoved[1]]
                myBoard.squares[pieceMoved[0]][pieceMoved[1]] = 0
                return True
        else:
            return False
