from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(491, 784)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 471, 771))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 35, 171, 21))
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 36, 131, 20))
        self.NomeApostador = QLineEdit(self.widget)
        self.NomeApostador.setObjectName(u"NomeApostador")
        self.NomeApostador.setGeometry(QRect(30, 60, 251, 20))
        self.ValorAposta = QLineEdit(self.widget)
        self.ValorAposta.setObjectName(u"ValorAposta")
        self.ValorAposta.setGeometry(QRect(320, 60, 113, 20))
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(40, 140, 82, 17))
        self.radioButton.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 180, 161, 16))
        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(150, 370, 31, 21))
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(270, 330, 16, 16))
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(200, 360, 61, 41))
        self.Apostar = QPushButton(self.widget)
        self.Apostar.setObjectName(u"Apostar")
        self.Apostar.setGeometry(QRect(170, 272, 121, 41))
        self.Apostar.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"font: 12pt \"Comic Sans MS\";")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 430, 181, 21))
        self.qtdapostadores = QLineEdit(self.widget)
        self.qtdapostadores.setObjectName(u"qtdapostadores")
        self.qtdapostadores.setGeometry(QRect(290, 430, 31, 20))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 520, 181, 31))
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 560, 411, 192))
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 0, 451, 31))
        self.label_15.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 110, 441, 21))
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 210, 61, 31))
        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(110, 210, 31, 21))
        self.lineEdit_7 = QLineEdit(self.widget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(390, 210, 31, 21))
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(290, 210, 81, 31))
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 370, 111, 31))
        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(320, 370, 131, 31))
        self.lineEdit_8 = QLineEdit(self.widget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(270, 370, 31, 21))
        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(200, 120, 61, 51))
        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(320, 140, 111, 17))
        self.Resultado = QPushButton(self.widget)
        self.Resultado.setObjectName(u"Resultado")
        self.Resultado.setGeometry(QRect(170, 470, 121, 41))
        self.Resultado.setStyleSheet(u"background-color: rgb(170, 170, 0);\n"
"font: 75 12pt \"Comic Sans MS\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Nome Apostador</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Valor da Aposta</span></p></body></html>", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Time Casa", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Escolha o Placar</span></p></body></html>", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">X</span></p></body></html>", None))
        self.Apostar.setText(QCoreApplication.translate("MainWindow", u"Apostar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Quantidade de Apostadores</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Ganhadores</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Apostas", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Premio", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#005500;\">BET-ADS</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Escolha o Vencedor</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Time Casa</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Time Visitante</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Gols do Time Casa</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Gols do Time Visitante</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">X</span></p></body></html>", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Time Visitante", None))
        self.Resultado.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
    # retranslateUi

        # self.Resultado.clicked.connect(self.gerar_placar)

def gerar_placar():
    gols_casa = random.randint(0, 5)
    gols_visitante = random.randint(0, 5)

    placar = [
        {"time": "Time da casa", "gols": gols_casa},
        {"time": "Time Visitante", "gols": gols_visitante}
    ]

    return placar

def exibir_placar(placar):
    print("Placar final:")
    for resultado in placar:
        print(f"{resultado['time']}: {resultado['gols']}")

def validar_vencedor(placar):
    if placar[0]['gols'] > placar[1]['gols']:
        return placar[0]['time']
    elif placar[1]['gols'] > placar[0]['gols']:
        return placar[1]['time']
    else:
        return "Empate"

placar = gerar_placar()
exibir_placar(placar)

ganhador = validar_vencedor(placar)
print(f"Vencedor: {ganhador} ganhou")