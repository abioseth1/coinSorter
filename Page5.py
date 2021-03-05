# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page5.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window5(object):
    def setupUi(self, Window5):
        Window5.setObjectName("Window5")
        Window5.resize(509, 600)
        Window5.setMinimumSize(QtCore.QSize(500, 600))
        self.centralwidget = QtWidgets.QWidget(Window5)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QFrame(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(0, 0, 510, 534))
        self.label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.label_1.setStyleSheet("background-color:rgb(51, 32, 74);")
        self.label_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_1.setObjectName("label_1")
        self.gridLayout = QtWidgets.QGridLayout(self.label_1)
        self.gridLayout.setObjectName("gridLayout")
        self.Header_Page5 = QtWidgets.QLabel(self.label_1)
        self.Header_Page5.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Header_Page5.setFont(font)
        self.Header_Page5.setStyleSheet("color: #FFF;")
        self.Header_Page5.setObjectName("Header_Page5")
        self.gridLayout.addWidget(self.Header_Page5, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.label_1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(62, 62, 62); color:rgb(170, 255, 165);")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.Main_Menu_Push_Button = QtWidgets.QPushButton(self.label_1)
        self.Main_Menu_Push_Button.setStyleSheet("QPushButton{\n"
"color:rgb(170, 255, 165);\n"
"background-color: rgb(62, 62, 62);\n"
"}")
        self.Main_Menu_Push_Button.setObjectName("Main_Menu_Push_Button")
        self.gridLayout.addWidget(self.Main_Menu_Push_Button, 2, 0, 1, 1)
        Window5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 26))
        self.menubar.setObjectName("menubar")
        Window5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window5)
        self.statusbar.setObjectName("statusbar")
        Window5.setStatusBar(self.statusbar)

        self.retranslateUi(Window5)
        QtCore.QMetaObject.connectSlotsByName(Window5)

    def retranslateUi(self, Window5):
        _translate = QtCore.QCoreApplication.translate
        Window5.setWindowTitle(_translate("Window5", "MainWindow"))
        self.Header_Page5.setText(_translate("Window5", "Program Configration"))
        self.textBrowser.setHtml(_translate("Window5", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The current currency setting is: p</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">p = pennies (GDP) </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cent(s) = cents (USD) </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">malagasey airey (MGA) </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The minimum coin input value is:  0</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The maximum coin input value is:  10000</p></body></html>"))
        self.Main_Menu_Push_Button.setText(_translate("Window5", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window5 = QtWidgets.QMainWindow()
    ui = Ui_Window5()
    ui.setupUi(Window5)
    Window5.show()
    sys.exit(app.exec_())
