from Board import Board
import Move

gameMode = 1
myBoard = Board()
myBoard.setup()
#while gameMode == 1:
print(myBoard)
Move.getAllMovementOptions(myBoard)
