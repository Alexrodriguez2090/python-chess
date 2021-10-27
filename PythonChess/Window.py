from PyQt5 import QtCore, QtGui, QtWidgets
from Piece import Piece

class Window(object):
    def setupUi(self, MainWindow, fullBoardPath):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setMouseTracking(True)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.Board.setStyleSheet(fullBoardPath)
        self.Board.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Board.setLineWidth(1)
        self.Board.setText("")
        self.Board.setPixmap(QtGui.QPixmap(fullBoardPath))
        self.Board.setScaledContents(True)
        self.Board.setObjectName("Board")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def connectPieces(self, myBoard):
        self.allPieces = []
        for row in myBoard:
            for square in row:
                if isinstance(square, Piece):
                    piece = square
                    self.allPieces.append(piece)
                    piece.hideMovesSignal.connect(self.removeMoves)
        return self.allPieces

    def removeMoves(self): #Change to remove only for the piece that was clicked on
        for piece in self.allPieces:
            for move in piece.showMoves:
                move.setVisible(False)

    def updatePieces(self, onBoardCoords):
        for visiblePiece in self.allPieces:
            if visiblePiece.currentPosition == onBoardCoords:
                visiblePiece.hide()

    def getCentralwidget(self):
        return self.centralwidget