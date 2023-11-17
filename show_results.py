def show_results(TEXT, lemma_list, pos_list, sorted_key_words_or_phrases):
    import os
    import signal
    import sys

    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QListWidgetItem

    import database_processing

    class Ui_MainWindowResult(object):
        def setupUi(self, MainWindowResult):
            interface_index = 1
            MainWindowResult.setObjectName("MainWindowResult")
            MainWindowResult.resize(600, 750)
            MainWindowResult.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap("Images/keyword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
            )
            MainWindowResult.setWindowIcon(icon)
            MainWindowResult.setStyleSheet("background-color: rgb(74, 74, 74);")
            self.centralwidget = QtWidgets.QWidget(MainWindowResult)
            self.centralwidget.setObjectName("centralwidget")

            self.keyword_label = QtWidgets.QLabel(self.centralwidget)
            self.keyword_label.setGeometry(QtCore.QRect(25, 35, 550, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            font.setStyleStrategy(QtGui.QFont.PreferDefault)
            self.keyword_label.setFont(font)
            self.keyword_label.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "\n" "background-color: rgb(21, 56, 54);"
            )
            self.keyword_label.setAlignment(QtCore.Qt.AlignCenter)
            self.keyword_label.setObjectName("keyword_label")

            self.listWidget = QtWidgets.QListWidget(self.centralwidget)
            self.listWidget.setGeometry(QtCore.QRect(25, 130, 550, 250))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            self.listWidget.setFont(font)
            self.listWidget.viewport().setProperty(
                "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor)
            )
            self.listWidget.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.listWidget.setAutoScroll(False)
            self.listWidget.setItemAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setObjectName("listWidget")

            self.add_result_button = QtWidgets.QPushButton(self.centralwidget)
            self.add_result_button.setGeometry(QtCore.QRect(100, 415, 400, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.add_result_button.setFont(font)
            self.add_result_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
            self.add_result_button.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.add_result_button.setObjectName("add_result_button")
            self.add_result_button.clicked.connect(
                lambda: database_processing.database_add_record()
            )
            self.add_result_button.clicked.connect(lambda: self.record_add_btn_hide())

            self.database_view_button = QtWidgets.QPushButton(self.centralwidget)
            self.database_view_button.setGeometry(QtCore.QRect(125, 500, 350, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.database_view_button.setFont(font)
            self.database_view_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
            self.database_view_button.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.database_view_button.setObjectName("database_view_button")
            self.database_view_button.clicked.connect(
                lambda: database_processing.run_threading()
            )
            self.database_view_button.clicked.connect(
                lambda: self.database_view_btn_hide()
            )

            self.exit_button = QtWidgets.QPushButton(self.centralwidget)
            self.exit_button.setGeometry(QtCore.QRect(200, 670, 200, 50))
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
            self.exit_button.clicked.connect(lambda: exit_program())

            self.new_text_select_button = QtWidgets.QPushButton(self.centralwidget)
            self.new_text_select_button.setGeometry(QtCore.QRect(150, 585, 300, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.new_text_select_button.setFont(font)
            self.new_text_select_button.setCursor(
                QtGui.QCursor(QtCore.Qt.OpenHandCursor)
            )
            self.new_text_select_button.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.new_text_select_button.setObjectName("new_text_select_button")
            self.new_text_select_button.clicked.connect(lambda: restart())

            MainWindowResult.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(MainWindowResult)
            self.statusbar.setObjectName("statusbar")
            MainWindowResult.setStatusBar(self.statusbar)

            for klme in sorted_key_words_or_phrases:
                item = QListWidgetItem(str(interface_index) + " - " + klme)
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.listWidget.addItem(item)
                interface_index += 1

            self.retranslateUi(MainWindowResult)
            self.listWidget.setCurrentRow(-1)
            QtCore.QMetaObject.connectSlotsByName(MainWindowResult)

        def retranslateUi(self, MainWindowResult):
            _translate = QtCore.QCoreApplication.translate
            MainWindowResult.setWindowTitle(
                _translate("MainWindowResult", "Keyword Extraction")
            )
            self.keyword_label.setText(_translate("MainWindowResult", "Keywords"))
            self.add_result_button.setText(
                _translate("MainWindowResult", "ADD RESULTS TO DATABASE")
            )
            self.database_view_button.setText(
                _translate("MainWindowResult", "SHOW DATABASE")
            )
            self.exit_button.setText(_translate("MainWindowResult", "EXIT PROGRAM"))
            self.new_text_select_button.setText(
                _translate("MainWindowResult", "SELECT A NEW TEXT")
            )

        def record_add_btn_hide(self):
            self.add_result_button.setHidden(True)

        def database_view_btn_hide(self):
            self.database_view_button.setHidden(True)

    def restart():
        os.execl(sys.executable, sys.executable, *sys.argv)

    def exit_program():
        sig = getattr(signal, "SIGKILL", signal.SIGTERM)
        os.kill(os.getpid(), sig)
        sys.exit()

    new_data = TEXT, lemma_list, pos_list, sorted_key_words_or_phrases
    database_processing.new_data_preprocessing(new_data)

    appResult = QtWidgets.QApplication(sys.argv)
    MainWindowResult = QtWidgets.QMainWindow()
    ui = Ui_MainWindowResult()
    ui.setupUi(MainWindowResult)
    MainWindowResult.show()
    sys.exit(appResult.exec_())
