# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pytesseract


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 622)
        MainWindow.setMinimumSize(QtCore.QSize(728, 622))
        MainWindow.setMaximumSize(QtCore.QSize(728, 622))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagePathEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.imagePathEdit.setEnabled(True)
        self.imagePathEdit.setGeometry(QtCore.QRect(10, 10, 381, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.imagePathEdit.setFont(font)
        self.imagePathEdit.setFrame(True)
        self.imagePathEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.imagePathEdit.setReadOnly(False)
        self.imagePathEdit.setClearButtonEnabled(True)
        self.imagePathEdit.setObjectName("imagePathEdit")
        self.textResultEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textResultEdit.setGeometry(QtCore.QRect(10, 40, 711, 551))
        self.textResultEdit.setObjectName("textResultEdit")
        self.textResultEdit.textChanged.connect(self.changeLen)
        self.typeLabel = QtWidgets.QLabel(self.centralwidget)
        self.typeLabel.setGeometry(QtCore.QRect(440, 10, 71, 21))
        self.typeLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.typeLabel.setObjectName("typeLabel")
        self.typeBox = QtWidgets.QComboBox(self.centralwidget)
        self.typeBox.setGeometry(QtCore.QRect(510, 10, 71, 22))
        self.typeBox.setAcceptDrops(False)
        self.typeBox.setObjectName("typeBox")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.readPush = QtWidgets.QPushButton(self.centralwidget)
        self.readPush.setGeometry(QtCore.QRect(590, 10, 51, 23))
        self.readPush.setObjectName("readPush")
        self.readPush.clicked.connect(self.readImage)
        self.textLenLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLenLabel.setGeometry(QtCore.QRect(10, 600, 61, 16))
        self.textLenLabel.setObjectName("textLenLabel")
        self.browsePush = QtWidgets.QPushButton(self.centralwidget)
        self.browsePush.setGeometry(QtCore.QRect(400, 10, 31, 23))
        self.browsePush.setAutoDefault(False)
        self.browsePush.setDefault(False)
        self.browsePush.setFlat(False)
        self.browsePush.setObjectName("browsePush")
        self.browsePush.clicked.connect(self.browseFiles)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(75, 598, 641, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Image Text Reader"))
        self.imagePathEdit.setText(_translate("MainWindow", "Image path"))
        self.textResultEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Text goes here</p></body></html>"))
        self.typeLabel.setText(_translate("MainWindow", "Type of text:"))
        self.typeBox.setItemText(0, _translate("MainWindow", "Type 1"))
        self.typeBox.setItemText(1, _translate("MainWindow", "Type 2"))
        self.typeBox.setItemText(2, _translate("MainWindow", "Type 3"))
        self.typeBox.setItemText(3, _translate("MainWindow", "Type 4"))
        self.typeBox.setItemText(4, _translate("MainWindow", "Type 5"))
        self.typeBox.setItemText(5, _translate("MainWindow", "Type 6"))
        self.typeBox.setItemText(6, _translate("MainWindow", "Type 7"))
        self.typeBox.setItemText(7, _translate("MainWindow", "Type 8"))
        self.typeBox.setItemText(8, _translate("MainWindow", "Type 9"))
        self.typeBox.setItemText(9, _translate("MainWindow", "Type 10"))
        self.typeBox.setItemText(10, _translate("MainWindow", "Type 11"))
        self.typeBox.setItemText(11, _translate("MainWindow", "Type 12"))
        self.readPush.setText(_translate("MainWindow", "Read"))
        self.textLenLabel.setText(_translate("MainWindow", "Text length:"))
        self.browsePush.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "14"))


    def browseFiles(self):
        self.imagePathEdit.setText(QtWidgets.QFileDialog.getOpenFileName()[0])

    def changeLen(self):
        self.label.setText(str(len(self.textResultEdit.toPlainText())))

    def readImage(self):
        try:
            if int(self.typeBox.currentText()[-2:]) == 1:
                factor = 0
            else:
                factor = 1
            text = pytesseract.image_to_string(self.imagePathEdit.text(
            ), config=f"--psm {int(self.typeBox.currentText()[-2:])+factor}")
            if len(text)==0:
                QtWidgets.QMessageBox.about(
                self.MainWindow, "Warning", "No characters were found")
            else:
                self.textResultEdit.setText(text)
        except pytesseract.pytesseract.TesseractError:
            QtWidgets.QMessageBox.about(
                self.MainWindow, "Warning", "Unsupported file format")
        except UnicodeDecodeError:
            QtWidgets.QMessageBox.about(
                self.MainWindow, "Warning", "Unsupported file format")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
