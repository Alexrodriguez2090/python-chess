from Board import Board
from Window import Window
from PyQt5 import QtWidgets
from MoveEngine import MoveEngine

import configparser
import sys

class Main:
    def __init__(self):

        config = configparser.ConfigParser()
        config.read("PythonChess/paths.ini")
        fullPiecesPath = config["DEFAULT"]["piecesPath"] + config["OPTIONS"]["piecesUsed"]
        fullBoardPath = config["DEFAULT"]["boardsPath"] + config["OPTIONS"]["boardUsed"]
        print(config['DEFAULT']["boardsPath"])

        if __name__ == "__main__":
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            self.ui = Window()
            self.ui.setupUi(MainWindow, fullBoardPath)

            self.myBoard = Board(fullPiecesPath)
            self.myBoard.setup(self.ui.getCentralwidget())
            self.Move = MoveEngine()
            self.Move.getLegalMoves(self.myBoard)

            visualPieces = self.ui.connectPieces(self.myBoard.squares)
            for piece in visualPieces:
                piece.boardMoveSignal.connect(self.movePieceSetup)
            MainWindow.show()
            sys.exit(app.exec_())

    def movePieceSetup(self, pieceMovedCoords, newCoords, onBoardCoords):
        print(newCoords)
        pieceMoved = self.myBoard.lookAtSquare(pieceMovedCoords)
        checkIfMoved = self.Move.movePiece(self.myBoard, pieceMoved, newCoords)
        if checkIfMoved:
            self.Move.getLegalMoves(self.myBoard)
            self.ui.updatePieces(onBoardCoords)


main = Main()