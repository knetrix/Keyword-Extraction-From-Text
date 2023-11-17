import os
import sys

from langdetect import detect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

current_dir = os.getcwd()

FILE_SELECT_NUMBER = 0
RIGHT = 2

STATE = ""

TEXT = ""

try:

    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(600, 380)
            MainWindow.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
            MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap(os.path.join(current_dir, "Images/keyword.png")),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off,
            )
            MainWindow.setWindowIcon(icon)
            MainWindow.setStyleSheet("background-color: rgb(74, 74, 74);")
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")

            self.text_1 = QtWidgets.QLabel(self.centralwidget)
            self.text_1.setGeometry(QtCore.QRect(25, 145, 550, 55))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            font.setStyleStrategy(QtGui.QFont.PreferDefault)
            self.text_1.setFont(font)
            self.text_1.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "\n" "background-color: rgb(21, 56, 54);"
            )
            self.text_1.setAlignment(QtCore.Qt.AlignCenter)
            self.text_1.setObjectName("text_1")

            self.file_select_button = QtWidgets.QPushButton(self.centralwidget)
            self.file_select_button.setGeometry(QtCore.QRect(225, 225, 150, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.file_select_button.setFont(font)
            self.file_select_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
            self.file_select_button.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.file_select_button.setObjectName("file_select_button")
            self.file_select_button.clicked.connect(file_select)

            self.exit_button = QtWidgets.QPushButton(self.centralwidget)
            self.exit_button.setGeometry(QtCore.QRect(200, 300, 200, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.exit_button.setFont(font)
            self.exit_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
            self.exit_button.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.exit_button.setObjectName("exit_button")
            self.exit_button.clicked.connect(exit_program)

            self.radio_button_ing = QtWidgets.QRadioButton(self.centralwidget)
            self.radio_button_ing.setGeometry(QtCore.QRect(175, 100, 100, 20))
            self.radio_button_ing.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "\n" "background-color: rgb(21, 56, 54);"
            )
            icon1 = QtGui.QIcon()
            icon1.addPixmap(
                QtGui.QPixmap(os.path.join(current_dir, "Images/england.png")),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off,
            )
            self.radio_button_ing.setIcon(icon1)
            self.radio_button_ing.setChecked(True)
            self.radio_button_ing.setObjectName("radio_button_ing")
            self.radio_button_ing.toggled.connect(self.selected_ing)

            self.radio_button_tur = QtWidgets.QRadioButton(self.centralwidget)
            self.radio_button_tur.setGeometry(QtCore.QRect(325, 100, 100, 20))
            self.radio_button_tur.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "\n" "background-color: rgb(21, 56, 54);"
            )
            icon2 = QtGui.QIcon()
            icon2.addPixmap(
                QtGui.QPixmap(os.path.join(current_dir, "Images/turkey.png")),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off,
            )
            self.radio_button_tur.setIcon(icon2)
            self.radio_button_tur.setIconSize(QtCore.QSize(20, 20))
            self.radio_button_tur.setObjectName("radio_button_tur")
            self.radio_button_tur.toggled.connect(self.selected_tur)

            self.text_2 = QtWidgets.QLabel(self.centralwidget)
            self.text_2.setGeometry(QtCore.QRect(25, 25, 550, 50))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            font.setStyleStrategy(QtGui.QFont.PreferDefault)
            self.text_2.setFont(font)
            self.text_2.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "\n" "background-color: rgb(21, 56, 54);"
            )
            self.text_2.setAlignment(QtCore.Qt.AlignCenter)
            self.text_2.setObjectName("text_2")

            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def selected_ing(self, selected):
            global STATE
            if selected:
                STATE = "Ing"

        def selected_tur(self, selected):
            global STATE
            if selected:
                STATE = "Tur"

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Keyword Extraction"))
            self.text_1.setText(
                _translate("MainWindow", "Please choose file of .txt format..")
            )
            self.file_select_button.setText(_translate("MainWindow", "Browse"))
            self.exit_button.setText(_translate("MainWindow", "Exit The Program"))
            self.radio_button_ing.setText(_translate("MainWindow", "English"))
            self.radio_button_tur.setText(_translate("MainWindow", "Turkish"))
            self.text_2.setText(_translate("MainWindow", "Select Language.."))

    def file_select():
        global FILE_SELECT_NUMBER
        global RIGHT
        global TEXT
        TEXT = ""

        def number_and_dot(text_line):
            TEXT_M = ""
            tmp = 0
            for letter in text_line:
                if letter.isnumeric():
                    tmp += 1
                    TEXT_M += letter
                    continue

                elif (letter == "." or letter == ",") and tmp > 0:
                    TEXT_M += letter
                    tmp = 0
                    continue

                elif (letter == "." or letter == ",") and tmp == 0:
                    TEXT_M += " ."
                else:
                    TEXT_M += letter
                    tmp = 0

            return TEXT_M

        os.chdir(os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop"))
        dir_desktop = os.getcwd()
        filters = "Text files (*.txt)"
        fileObj = QFileDialog.getOpenFileName(
            None, " File Select Window ", dir_desktop, filters
        )

        extension = fileObj[0][-3:]

        def message_box_exit(msg: str):
            msg_box_obj = QMessageBox()
            msg_box_obj.setIcon(QMessageBox.Critical)
            msg_box_obj.setWindowTitle("Exiting Program")
            msg_box_obj.setText(msg + " Exiting the Program..")
            msg_box_obj.exec_()
            sys.exit()

        def message_box_remain(msg: str, right: int):
            msg_box_obj = QMessageBox()
            msg_box_obj.setIcon(QMessageBox.Critical)
            msg_box_obj.setText(msg)
            msg_box_obj.setInformativeText("Remaining Rights: " + str(right))
            msg_box_obj.setWindowTitle("Error")
            msg_box_obj.exec_()
            global RIGHT
            RIGHT = right - 1
            file_select()

        if extension != "txt" and extension != "":
            message_box_exit("Incorrect Extension!")

        elif fileObj[1] != "":
            with open(fileObj[0], "r", encoding="utf-8") as file_txt:
                for line in file_txt.readlines():
                    if line != "\n":
                        if line[-2] != ".":
                            line = line[:-1]
                            line += " .\n"

                        line = number_and_dot(line)

                    TEXT = TEXT + str(line.strip()) + " "
                if TEXT == "":
                    message_box_exit("File Content is Empty!")

        else:
            if 0 < RIGHT <= 2:
                message_box_remain(
                    "You are exiting without selecting a file! Please select a file..",
                    RIGHT,
                )
            else:
                message_box_exit("Limit Crossed!")

        detect_language = detect(TEXT)

        if (STATE in {"Ing", ""}) and detect_language == "tr":
            if RIGHT == 0:
                message_box_exit("Limit Crossed!")
            message_box_remain(
                "Language Selection and Text Language don't Match, Please select the file again!\nText Language: Turkish",
                RIGHT,
            )

        elif (STATE == "Tur") and detect_language == "en":
            if RIGHT == 0:
                message_box_exit("Limit Crossed!")
            message_box_remain(
                "Language Selection and Text Language don't Match, Please select the file again!\nText Language: English",
                RIGHT,
            )

        elif detect_language != "tr" and detect_language != "en":
            if RIGHT == 0:
                message_box_exit("Limit Crossed!")
            message_box_remain(
                "Language Selection and Text Language don't Match, Please select the file again!\nText Language: Unknown",
                RIGHT,
            )

        FILE_SELECT_NUMBER += 1
        app.exit(app.exec())

    def exit_program():
        sys.exit()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exit(app.exec())
    MainWindow.close()
    if FILE_SELECT_NUMBER == 0:
        raise SystemError("Exited Program!")

except SystemError as s:
    print(s)
    sys.exit()
except Exception as e:
    print("An error occurred while selecting a file! ", e)
    sys.exit()
else:
    print("\n\nFile Selection Successful! The Program Continues..\n")

    print()
    print("Original Text: \n" + TEXT)
    print()
    os.chdir(current_dir)
