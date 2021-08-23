from Board import Board
import Move

gameMode = 1
myBoard = Board()
myBoard.setup()
#while gameMode == 1:
print(myBoard)
Move.getLegalMoves(myBoard, "black")
print(myBoard.lookAtSquare((1, 0)).legalOptions)
print(myBoard.lookAtSquare((1, 1)).legalOptions)
print(myBoard.lookAtSquare((1, 2)).legalOptions)
print(myBoard.lookAtSquare((1, 3)).legalOptions)
print(myBoard.lookAtSquare((1, 4)).legalOptions)
print(myBoard.lookAtSquare((1, 5)).legalOptions)
print(myBoard.lookAtSquare((1, 6)).legalOptions)
print(myBoard.lookAtSquare((1, 7)).legalOptions)
