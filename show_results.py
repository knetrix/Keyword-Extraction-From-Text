def Show_results(metin, metin_lemma, metin_token_pos, siralanmis_anahtar_kelimeler):
    import database_processing
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QListWidgetItem
    import sys
    import os
    import signal  # Flask web serverin kapanması için eklendi

    class Ui_MainWindowSonuc(object):
        def setupUi(self, MainWindowSonuc):
            arayuz_indeks = 1
            MainWindowSonuc.setObjectName("MainWindowSonuc")
            MainWindowSonuc.resize(600, 750)
            MainWindowSonuc.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap("Images/keyword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
            )
            MainWindowSonuc.setWindowIcon(icon)
            MainWindowSonuc.setStyleSheet("background-color: rgb(74, 74, 74);")
            self.centralwidget = QtWidgets.QWidget(MainWindowSonuc)
            self.centralwidget.setObjectName("centralwidget")

            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(25, 35, 550, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            font.setStyleStrategy(QtGui.QFont.PreferDefault)
            self.label.setFont(font)
            self.label.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "\n" "background-color: rgb(21, 56, 54);"
            )
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")

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

            self.SonucEkleButon = QtWidgets.QPushButton(self.centralwidget)
            self.SonucEkleButon.setGeometry(QtCore.QRect(100, 415, 400, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.SonucEkleButon.setFont(font)
            self.SonucEkleButon.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
            self.SonucEkleButon.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.SonucEkleButon.setObjectName("SonucEkleButon")
            self.SonucEkleButon.clicked.connect(
                lambda: database_processing.veritabani_kayit_ekle()
            )
            self.SonucEkleButon.clicked.connect(lambda: self.Kayit_ekle_btn_gizle())

            self.VeritabaniGoruntuleButon = QtWidgets.QPushButton(self.centralwidget)
            self.VeritabaniGoruntuleButon.setGeometry(QtCore.QRect(125, 500, 350, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.VeritabaniGoruntuleButon.setFont(font)
            self.VeritabaniGoruntuleButon.setCursor(
                QtGui.QCursor(QtCore.Qt.OpenHandCursor)
            )
            self.VeritabaniGoruntuleButon.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.VeritabaniGoruntuleButon.setObjectName("VeritabaniGoruntuleButon")
            self.VeritabaniGoruntuleButon.clicked.connect(
                lambda: database_processing.calistir_threading()
            )
            self.VeritabaniGoruntuleButon.clicked.connect(
                lambda: self.Veritabani_Goruntule_btn_gizle()
            )

            self.CikButon = QtWidgets.QPushButton(self.centralwidget)
            self.CikButon.setGeometry(QtCore.QRect(200, 670, 200, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.CikButon.setFont(font)
            self.CikButon.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
            self.CikButon.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.CikButon.setObjectName("CikButon")
            self.CikButon.clicked.connect(lambda: programdan_cik())

            self.YeniMetinSecButon = QtWidgets.QPushButton(self.centralwidget)
            self.YeniMetinSecButon.setGeometry(QtCore.QRect(150, 585, 300, 50))
            font = QtGui.QFont()
            font.setFamily("Rockwell")
            font.setPointSize(14)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.YeniMetinSecButon.setFont(font)
            self.YeniMetinSecButon.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
            self.YeniMetinSecButon.setStyleSheet(
                "color: rgb(255, 181, 32);\n" "background-color: rgb(21, 56, 54);"
            )
            self.YeniMetinSecButon.setObjectName("YeniMetinSecButon")
            self.YeniMetinSecButon.clicked.connect(lambda: yeniden_baslat())

            MainWindowSonuc.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(MainWindowSonuc)
            self.statusbar.setObjectName("statusbar")
            MainWindowSonuc.setStatusBar(self.statusbar)

            for klme in siralanmis_anahtar_kelimeler:
                item = QListWidgetItem(str(arayuz_indeks) + " - " + klme)
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.listWidget.addItem(item)
                arayuz_indeks += 1

            self.retranslateUi(MainWindowSonuc)
            self.listWidget.setCurrentRow(-1)
            QtCore.QMetaObject.connectSlotsByName(MainWindowSonuc)

        def retranslateUi(self, MainWindowSonuc):
            _translate = QtCore.QCoreApplication.translate
            MainWindowSonuc.setWindowTitle(
                _translate("MainWindowSonuc", "Keyword Extraction")
            )
            self.label.setText(_translate("MainWindowSonuc", "Keywords"))
            self.SonucEkleButon.setText(
                _translate("MainWindowSonuc", "ADD RESULTS TO DATABASE")
            )
            self.VeritabaniGoruntuleButon.setText(
                _translate("MainWindowSonuc", "SHOW DATABASE")
            )
            self.CikButon.setText(_translate("MainWindowSonuc", "EXIT PROGRAM"))
            self.YeniMetinSecButon.setText(
                _translate("MainWindowSonuc", "SELECT A NEW TEXT")
            )

        def Kayit_ekle_btn_gizle(self):
            self.SonucEkleButon.setHidden(True)

        def Veritabani_Goruntule_btn_gizle(self):
            self.VeritabaniGoruntuleButon.setHidden(True)

    def yeniden_baslat():
        os.execl(sys.executable, sys.executable, *sys.argv)

    def programdan_cik():
        sig = getattr(signal, "SIGKILL", signal.SIGTERM)
        os.kill(os.getpid(), sig)  # Flask web serveri Kapat - os.kill() fonksiyonu
        sys.exit()  # Programı kapat

    database_processing.degiskenleri_al(
        metin, metin_lemma, metin_token_pos, siralanmis_anahtar_kelimeler
    )
    appSonuc = QtWidgets.QApplication(sys.argv)
    MainWindowSonuc = QtWidgets.QMainWindow()
    ui = Ui_MainWindowSonuc()
    ui.setupUi(MainWindowSonuc)
    MainWindowSonuc.show()
    sys.exit(appSonuc.exec_())
