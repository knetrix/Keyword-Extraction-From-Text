import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from langdetect import detect

current_dir = os.getcwd()

FILE_SELECT_NUMBER = 0
RIGHT = 2

STATE = ""

TEXT = ""

try:

    class Ui_MainWindow(object):
        durum = "Ing"

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

            self.label_1 = QtWidgets.QLabel(self.centralwidget)
            self.label_1.setGeometry(QtCore.QRect(25, 145, 550, 55))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            font.setStyleStrategy(QtGui.QFont.PreferDefault)
            self.label_1.setFont(font)
            self.label_1.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "\n" "background-color: rgb(21, 56, 54);"
            )
            self.label_1.setAlignment(QtCore.Qt.AlignCenter)
            self.label_1.setObjectName("label")

            self.FileSelectButton = QtWidgets.QPushButton(self.centralwidget)
            self.FileSelectButton.setGeometry(QtCore.QRect(225, 225, 150, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.FileSelectButton.setFont(font)
            self.FileSelectButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
            self.FileSelectButton.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.FileSelectButton.setObjectName("FileSelectButton")
            self.FileSelectButton.clicked.connect(file_select)

            self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
            self.ExitButton.setGeometry(QtCore.QRect(200, 300, 200, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.ExitButton.setFont(font)
            self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
            self.ExitButton.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.ExitButton.setObjectName("ExitButton")
            self.ExitButton.clicked.connect(exit_program)

            self.radioButton_Ing = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_Ing.setGeometry(QtCore.QRect(175, 100, 100, 20))
            self.radioButton_Ing.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "\n" "background-color: rgb(21, 56, 54);"
            )
            icon1 = QtGui.QIcon()
            icon1.addPixmap(
                QtGui.QPixmap(os.path.join(current_dir, "Images/england.png")),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off,
            )
            self.radioButton_Ing.setIcon(icon1)
            self.radioButton_Ing.setChecked(True)
            self.radioButton_Ing.setObjectName("radioButton_Ing")
            self.radioButton_Ing.toggled.connect(self.selected_ing)

            self.radioButton_Tur = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_Tur.setGeometry(QtCore.QRect(325, 100, 100, 20))
            self.radioButton_Tur.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "\n" "background-color: rgb(21, 56, 54);"
            )
            icon2 = QtGui.QIcon()
            icon2.addPixmap(
                QtGui.QPixmap(os.path.join(current_dir, "Images/turkey.png")),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off,
            )
            self.radioButton_Tur.setIcon(icon2)
            self.radioButton_Tur.setIconSize(QtCore.QSize(20, 20))
            self.radioButton_Tur.setObjectName("radioButton_Tur")
            self.radioButton_Tur.toggled.connect(self.selected_tur)

            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(25, 25, 550, 50))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            font.setStyleStrategy(QtGui.QFont.PreferDefault)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "\n" "background-color: rgb(21, 56, 54);"
            )
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
            self.label_2.setObjectName("label_2")

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
            self.label_1.setText(
                _translate("MainWindow", "Please choose file of .txt format..")
            )
            self.FileSelectButton.setText(_translate("MainWindow", "Browse"))
            self.ExitButton.setText(_translate("MainWindow", "Exit The Program"))
            self.radioButton_Ing.setText(_translate("MainWindow", "English"))
            self.radioButton_Tur.setText(_translate("MainWindow", "Turkish"))
            self.label_2.setText(_translate("MainWindow", "Select Language.."))

    def file_select():
        global FILE_SELECT_NUMBER
        global RIGHT
        global TEXT
        TEXT = ""

        def number_and_dot(txtt):
            TEXT_M = ""
            tmp = 0
            for letter in txtt:
                if letter.isnumeric() == True:
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

        extension = fileObj[0][-3:]  # fileObj[0] -> selected txt file's path

        def message_box(msg: str):
            msg_box_obj = QMessageBox()
            msg_box_obj.setIcon(QMessageBox.Critical)
            msg_box_obj.setWindowTitle("Exiting Program")
            msg_box_obj.setText(msg + " Exiting the Program..")
            msg_box_obj.exec_()
            sys.exit()

        def message_box_2(msg: str, right: int):
            file_select_cancel = QMessageBox()
            file_select_cancel.setIcon(QMessageBox.Critical)
            file_select_cancel.setText(msg)
            file_select_cancel.setInformativeText("Remaining Rights: " + str(right))
            file_select_cancel.setWindowTitle("Error")
            file_select_cancel.exec_()
            global RIGHT
            RIGHT = right - 1
            file_select()

        if extension != "txt" and extension != "":
            message_box("Incorrect Extension!")

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
                    message_box("File Content is Empty!")

        else:
            if 0 < RIGHT <= 2:
                message_box_2(
                    "You are exiting without selecting a file! Please select a file..",
                    RIGHT,
                )
            else:
                message_box("Limit Crossed!")

        detect_language = detect(TEXT)

        if (STATE == "Ing" or STATE == "") and detect_language == "tr":
            if RIGHT == 0:
                message_box("Limit Crossed!")
            message_box_2(
                "Language Selection and Text Language don't Match, Please select the file again!\nText Language: Turkish",
                RIGHT,
            )

        elif (STATE == "Tur") and detect_language == "en":
            if RIGHT == 0:
                message_box("Limit Crossed!")
            message_box_2(
                "Language Selection and Text Language don't Match, Please select the file again!\nText Language: English",
                RIGHT,
            )

        elif detect_language != "tr" and detect_language != "en":
            if RIGHT == 0:
                message_box("Limit Crossed!")
            message_box_2(
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
