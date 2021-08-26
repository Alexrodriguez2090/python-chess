from Board import Board
from Window import Window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSvg import QSvgWidget
import Move
import sys

from Bishop import Bishop

gameMode = 0
myBoard = Board()
myBoard.setup()
colorPlaying = "white"
Move.getLegalMoves(myBoard, colorPlaying)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    ui.setupUi(MainWindow)
    ui.addPieces(MainWindow, myBoard.squares)
    MainWindow.show()
    sys.exit(app.exec_())

while gameMode == 0:
    print("Welcome to Python Chess")
    print("1. Play")
    print("2. Exit")
    if choice == "1" or choice == "play" or choice == "p":
        gameMode = 1
        while gameMode == 1:
            print(myBoard)
            move = input()

            pieceMoved = (int(move[0]), int(move[1]))
            squareMovedTo = (int(move[3]), int(move[4]))

            success = Move.movePiece(myBoard, pieceMoved, squareMovedTo, colorPlaying)

            if success == True:
                if colorPlaying == "white":
                    colorPlaying = "black"
                else:
                    colorPlaying = "white"
            Move.getLegalMoves(myBoard, colorPlaying)
    elif choice == "2" or choice == "quit" or choice == "exit":
        sys.exit()
