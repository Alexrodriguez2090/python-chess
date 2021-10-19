from Piece import Piece
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from King import King
from Pawn import Pawn

class Board:
    def __init__(self):
        self.squares = [[0]*8 for _ in range(8)]

    def setup(self): #add to init?
        rowNum = 0
        for row in self.squares:
            if rowNum == 0: #Black's backline
                row[0] = Rook("black", (rowNum, 0))
                row[1] = Knight("black", (rowNum, 1))
                row[2] = Bishop("black", (rowNum, 2))
                row[3] = Queen("black", (rowNum, 3))
                row[4] = King("black", (rowNum, 4))
                row[5] = Bishop("black", (rowNum, 5))
                row[6] = Knight("black", (rowNum, 6))
                row[7] = Rook("black", (rowNum, 7))
            elif rowNum == 1: #Black's pawnline
                for rowSquare in range(8):
                    row[rowSquare] = Pawn("black", (rowNum, rowSquare))
            elif rowNum == 6: #White's pawnline
                for rowSquare in range(8):
                    row[rowSquare] = Pawn("white", (rowNum, rowSquare))
            elif rowNum == 7: #White's backline
                row[0] = Rook("white", (rowNum, 0))
                row[1] = Knight("white", (rowNum, 1))
                row[2] = Bishop("white", (rowNum, 2))
                row[3] = Queen("white", (rowNum, 3))
                row[4] = King("white", (rowNum, 4))
                row[5] = Bishop("white", (rowNum, 5))
                row[6] = Knight("white", (rowNum, 6))
                row[7] = Rook("white", (rowNum, 7))
            rowNum += 1

    def lookAtSquare(self, coords):
        return self.squares[coords[0]][coords[1]]

    def __str__(self):
        stringSequence = ""
        rowNum = 0
        for row in self.squares:
            stringSequence += str(rowNum) + str(row) + "\n"
            rowNum += 1
        stringSequence += "  0, 1, 2, 3, 4, 5, 6, 7"
        stringSequence += "  a, b, c, d, e, f, g, h"
        return stringSequence

    def __call__(self):
        return self.squares
