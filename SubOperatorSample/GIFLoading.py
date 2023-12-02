# GIFLoading.py

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys


class LoadingGif(object):

    def mainUI(self, FrontWindow, gif_file):
        FrontWindow.setObjectName("FTwindow")

        # Set the window size based on the GIF resolution
        gif_width = 1090
        gif_height = 780
        FrontWindow.resize(gif_width + 50, gif_height + 50)

        self.centralwidget = QtWidgets.QWidget(FrontWindow)
        self.centralwidget.setObjectName("main-widget")

        # Label Create
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, gif_width, gif_height))
        self.label.setMinimumSize(QtCore.QSize(gif_width, gif_height))
        self.label.setMaximumSize(QtCore.QSize(gif_width, gif_height))
        self.label.setObjectName("lb1")
        FrontWindow.setCentralWidget(self.centralwidget)

        # Loading the GIF with the specified file name
        self.movie = QMovie(f"Assets/{gif_file}.gif")
        self.label.setMovie(self.movie)

        self.startAnimation()

    # Start Animation
    def startAnimation(self):
        self.movie.start()

    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()


def show_loading_gif(gif_file):
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    demo = LoadingGif()
    demo.mainUI(window, gif_file)
    window.show()
    sys.exit(app.exec_())
