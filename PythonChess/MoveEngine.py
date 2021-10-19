from PyQt5.QtCore import pyqtSlot
from Board import Board
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
        self.colorPlaying = "white"
        self.allPieces = []

        self.rookMoves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.bishopMoves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        self.knightMoves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

        self.pawnMovesWhite = [(1, 1), (1, -1)]
        self.pawnAttacksWhite = [(-1, 1), (-1, -1)]

        self.pawnMovesBlack = [(-1, 1), (-1, -1)]
        self.pawnAttacksBlack = [(1, 1), (1, -1)]
    
    def getLegalMoves(self, myBoard):
        self.getListOfAllPieces(myBoard) #Make this not iterate over every turn ?
        self.getAllMovementOptions(myBoard) #Same as above, as it updates every time

        king = self.getAllyKingPiece()
        oppKing = self.getOppKingPiece()
        testBoard = copy.deepcopy(myBoard)
        print(self.colorPlaying)
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
    
    #Checks that wherever the piece is moved, an OPPOSING piece isn't attacking the king
    def _getLegalMoves(self, testBoard, myMove, piece, king, oppKing):
        squareMovedTo = testBoard.squares[myMove[0]][myMove[1]]
        testBoard.squares[myMove[0]][myMove[1]] = testBoard.lookAtSquare(piece.place)
        testBoard.squares[piece.place[0]][piece.place[1]] = 0

        for move in self.bishopMoves:
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

        for move in self.knightMoves:
            kingSquare = king.place
            if king.checkInbounds(kingSquare):
                if isinstance(testBoard.lookAtSquare(kingSquare), Knight):
                    if self.colorPlaying != testBoard.lookAtSquare(kingSquare).color:
                        return

        for move in self.rookMoves:
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

        if self.colorPlaying == "white":
            for move in self.pawnAttacksBlack:
                kingSquare = king.place
                if king.checkInbounds(kingSquare):
                    if isinstance(testBoard.lookAtSquare(kingSquare), Pawn):
                        if self.colorPlaying != testBoard.lookAtSquare(kingSquare).color:
                            return
        else:
            for move in self.pawnAttacksWhite:
                kingSquare = king.place
                if king.checkInbounds(kingSquare):
                    if isinstance(testBoard.lookAtSquare(kingSquare), Pawn):
                        if self.colorPlaying != testBoard.lookAtSquare(kingSquare).color:
                            return

        piece.legalOptions.append(myMove)
 
    def movePiece(self, myBoard, pieceMoved, squareMovedTo):
        print(squareMovedTo)
        print(pieceMoved.legalOptions)
        print()
        print(self.colorPlaying)
        print(pieceMoved.color)
        if squareMovedTo in pieceMoved.legalOptions and self.colorPlaying == pieceMoved.color:
            squareMovedFrom = pieceMoved.place

            myBoard.squares[squareMovedTo[0]][squareMovedTo[1]] = pieceMoved
            pieceMoved.place = squareMovedTo

            myBoard.squares[squareMovedFrom[0]][squareMovedFrom[1]] = 0
            self.changeColorPlaying()
            print(myBoard)
            return True
        else:
            return False
    
    def changeColorPlaying(self):
        if self.colorPlaying == "white":
            self.colorPlaying = "black"
        else:
            self.colorPlaying = "white"



    def getAllMovementOptions(self, myBoard):
        for piece in self.allPieces:
            piece.getMovementOptions(myBoard)

    def getListOfAllPieces(self, myBoard):
        self.allPieces = []
        for row in myBoard.squares:
            for square in row:
                if isinstance(square, Piece):
                    self.allPieces.append(square)

    def getAllyKingPiece(self):
        for piece in self.allPieces:
            if isinstance(piece, King) and piece.color == self.colorPlaying:
                return piece

    def getOppKingPiece(self):
        for piece in self.allPieces:
            if isinstance(piece, King) and piece.color != self.colorPlaying:
                return piece