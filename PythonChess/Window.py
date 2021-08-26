from PyQt5 import QtCore, QtGui, QtWidgets
from Piece import Piece

class MovingObject(QtWidgets.QLabel):
    clickedSignal = QtCore.pyqtSignal()
    def __init__(self, centralwidget, movewidget, piece, x, y, r):
        super().__init__(centralwidget)

        self.centralwidget = centralwidget
        self.legalOptions = piece.legalOptions
        self.imageLink = piece.imageLink
        self.ratio = r
        self.ratioHalf = r / 2

        self.setGeometry(x, y, r, r)
        self.setPixmap(QtGui.QPixmap(self.imageLink))
        self.setMouseTracking(True)
        self.setScaledContents(True)

        self.showMoves = []

    def mousePressEvent(self, event):
        self.clickedSignal.emit()
        self.showMoves = []
        for move in self.legalOptions:
            movePicture = QtWidgets.QLabel(self.centralwidget)
            movePicture.setGeometry(QtCore.QRect(move[1] * 75, move[0] * 75, self.ratio, self.ratio))
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
        print(f"x: {self.pos().x()}, y: {self.pos().y()}")

class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1800, 1800))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setMouseTracking(True)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.movewidget = QtWidgets.QWidget(MainWindow)
        self.movewidget.setObjectName("movewidget")
        self.Board = QtWidgets.QLabel(self.centralwidget)
        self.Board.setEnabled(True)
        self.Board.setGeometry(QtCore.QRect(0, 0, 600, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Board.sizePolicy().hasHeightForWidth())
        self.Board.setSizePolicy(sizePolicy)
        self.Board.setMinimumSize(QtCore.QSize(500, 500))
        self.Board.setSizeIncrement(QtCore.QSize(1, 1))
        self.Board.setBaseSize(QtCore.QSize(500, 500))
        self.Board.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Board.setMouseTracking(True)
        self.Board.setAutoFillBackground(True)
        self.Board.setStyleSheet("images/boards/wood.jpg")
        self.Board.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Board.setLineWidth(1)
        self.Board.setText("")
        self.Board.setPixmap(QtGui.QPixmap("images/boards/wood.jpg"))
        self.Board.setScaledContents(True)
        self.Board.setObjectName("Board")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def addMoves(piece):
        for move in piece.legalOptions:
            movePicture = QtWidgets.QLabel(piece.movewidget)
            movePicture.setGeometry(QtCore.QRect(move[1] * 75, move[0] * 75, piece.ratio, piece.ratio))
            movePicture.setPixmap(QtGui.QPixmap(piece.imageLink))
            movePicture.setScaledContents(True)

    def removeMoves(self):
        for piece in self.allPieces:
            for move in piece.showMoves:
                move.setVisible(False)

    def addPieces(self, MainWindow, myBoard):
        self.allPieces = []
        for row in myBoard:
            for square in row:
                if isinstance(square, Piece):
                    piece = MovingObject(self.centralwidget, self.movewidget, square, square.place[1] * 75, square.place[0] * 75, 75)
                    self.allPieces.append(piece)
                    for piece in self.allPieces:
                        piece.clickedSignal.connect(self.removeMoves)
