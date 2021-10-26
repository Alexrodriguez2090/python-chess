from PyQt5 import QtCore, QtGui, QtWidgets

class Piece(QtWidgets.QLabel):
    hideMovesSignal = QtCore.pyqtSignal()
    boardMoveSignal = QtCore.pyqtSignal(tuple, tuple, tuple)

    def __init__(self, color, place, centralwidget):
        super().__init__(centralwidget)

        self.centralwidget = centralwidget
        self.ratio = 75
        self.ratioHalf = self.ratio / 2
        self.currentPosition = (place[1] * 75, place[0] * 75)

        self.color = color
        self.place = place
        self.movementOptions = []
        self.viableOptions = []
        self.legalOptions = []

        self.setGeometry(self.currentPosition[0], self.currentPosition[1], self.ratio, self.ratio)
        self.setPixmap(QtGui.QPixmap(self.imageLink))
        self.setMouseTracking(True)
        self.setScaledContents(True)

        self.showMoves = []

    def mousePressEvent(self, event):
        self.hideMovesSignal.emit()
        self.showMoves = []
        for move in self.legalOptions:
            movePicture = QtWidgets.QLabel(self.centralwidget)
            movePicture.setGeometry(QtCore.QRect(move[1] * self.ratio, move[0] * self.ratio, self.ratio, self.ratio))
            movePicture.setPixmap(QtGui.QPixmap(self.imageLink))
            movePicture.setScaledContents(True)
            movePicture.setVisible(True)
            self.showMoves.append(movePicture)

    def mouseMoveEvent(self, event):
        if not(event.buttons() & QtCore.Qt.LeftButton):
            return
        else:
            self.move(self.pos().x() + event.pos().x() - self.ratioHalf, self.pos().y() + event.pos().y() - self.ratioHalf)
        
    def mouseReleaseEvent(self, event):
        moved = False
        for move in self.legalOptions:
            moveX = move[1] * self.ratio
            moveY = move[0] * self.ratio
            if abs(moveX - self.pos().x()) < self.ratioHalf and abs(moveY - self.pos().y()) < self.ratioHalf:
                newCoords = (move[0], move[1])
                onBoardCoords = (moveX, moveY)

                self.boardMoveSignal.emit(self.place, newCoords, onBoardCoords) #Invoke MoveEngine.movePiece
                self.hideMovesSignal.emit()

                moved = True
                self.currentPosition = (onBoardCoords)
                self.move(moveX, moveY)
                break

        if moved == False:
            self.move(self.currentPosition[0], self.currentPosition[1])

        print(f"x: {self.pos().x()}, y: {self.pos().y()}")
    
    def __repr__(self):
        return self.icon
    
    def __getstate__(self):
        return self.__dict__.copy()

    def checkInbounds(self, coords):
        if 0 <= coords[0] <= 7 and 0 <= coords[1] <= 7:
            return True
        else:
            return False

    def blankMovementOptions(self):
        self.movementOptions = []
        self.viableOptions = []
        self.legalOptions = []