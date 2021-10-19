import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

from Piece import Piece

class TkWindow:
    window = tk.Tk()
    windowWidth = 600
    windowHeight = 600

    frame = Frame(window)
    frame.pack()

    canvas = Canvas(frame, bg = "black", width = 600, height = 600)
    canvas.pack()

    def __init__(self, chessboard):
        self.window.title("Python Chess")
        self.window.geometry(f"{self.windowWidth}x{self.windowHeight}")

        board = ImageTk.PhotoImage(Image.open("images/boards/wood.jpg").resize((self.windowWidth, self.windowHeight), Image.ANTIALIAS))
        self.canvas.create_image(300, 300, image = board)

        self.piecesList = []

        #character = PhotoImage(file="hero.png")
        #canvas.create_image(30,30,image=character)
        #boardImg = ImageTk.PhotoImage(Image.open("images/boards/wood.jpg").resize((self.windowWidth, self.windowHeight), Image.ANTIALIAS))
        #boardBackground = tk.Label(image=boardImg)
        #boardBackground.image = boardImg
        #boardBackground.place(x = -2, y = -2)
        self.addPieces(chessboard)
        self.window.mainloop()

    def addPieces(self, chessboard):
        for row in chessboard:
            for square in row:
                if isinstance(square, Piece):
                    piece = ImageTk.PhotoImage(Image.open(chessboard[0][0].imageLink).resize((75, 75)))
                    self.piecesList.append(piece)
                    self.canvas.create_image(75/2 + chessboard[0][0].place[1] * 75, 75/2 + chessboard[0][0].place[0] * 75, image = piece)
                    #pieceImg = ImageTk.PhotoImage(Image.open(square.imageLink).resize((75, 75)))
                    #piece = tk.Label(image=pieceImg)
                    #piece.image = pieceImg
                    #piece.place(x = square.place[1] * 75, y = square.place[0] * 75)

    def updatePieces(self, chessboard):
        for row in chessboard:
            for square in row:
                if isinstance(square, Piece):
                    pass