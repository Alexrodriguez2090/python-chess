from Board import Board
from Window import Window, MovingObject
from PyQt5 import QtCore, QtGui, QtWidgets
from MoveEngine import MoveEngine
import sys

class Main:
    def __init__(self):
        self.myBoard = Board()
        self.myBoard.setup()
        self.Move = MoveEngine()
        self.Move.getLegalMoves(self.myBoard)

        if __name__ == "__main__":
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Window()
            ui.setupUi(MainWindow)
            visualPieces = ui.addPieces(MainWindow, self.myBoard.squares)
            for piece in visualPieces:
                piece.boardMoveSignal.connect(self.movePieceSetup)
            MainWindow.show()
            sys.exit(app.exec_())

    def movePieceSetup(self, pieceMoved, newCoords):
        print(newCoords)
        actualMoveCheck = self.Move.movePiece(self.myBoard, pieceMoved, newCoords)
        if actualMoveCheck:
            self.Move.getLegalMoves(self.myBoard)


main = Main()