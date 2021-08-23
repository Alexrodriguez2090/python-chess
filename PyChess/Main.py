from Board import Board
import Move
import sys

gameMode = 0
myBoard = Board()
myBoard.setup()
colorPlaying = "white"
Move.getLegalMoves(myBoard, colorPlaying)

while gameMode == 0:
    print("Welcome to PyChess")
    print("1. Play")
    print("2. Exit")
    choice = input().lower()
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
