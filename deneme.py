# from file_selection_process import TEXT, STATE

from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
import sys
import threading
import time


def deneme():
    print("fonk")


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Close")

        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)

        # creating a label widget
        self.label = QLabel("Icon is set", self)

        # moving position
        self.label.move(100, 100)

        # setting up border
        self.label.setStyleSheet("border: 1px solid black;")

        # show all the widgets
        self.show()

        
        t1 = threading.Thread(target=deneme)
        t1.start()
        sys.exit()

        # closing the window
        #self.close()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app

App.exec_()

