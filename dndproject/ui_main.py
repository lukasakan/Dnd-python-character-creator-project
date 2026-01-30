from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setBaseSize(QtCore.QSize(20, 20))
        MainWindow.setStyleSheet("QMainWindow {"
                                 "background-image: url('images/pngtree-dungeon-with-large-dragons-near-it-on-fire-picture-image_2875224.jpg');"
                                 "background-repeat: no-repeat;"
                                 "background-position: center;"
                                 "}")
        

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harrington")
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dungeonsanddragons = QtWidgets.QLabel(self.centralwidget)
        self.dungeonsanddragons.setGeometry(QtCore.QRect(480, -10, 301, 141))
        self.dungeonsanddragons.setText("")
        self.dungeonsanddragons.setPixmap(QtGui.QPixmap("images/Dungeons-Dragons-Logo-2000.png"))
        self.dungeonsanddragons.setScaledContents(True)
        self.dungeonsanddragons.setIndent(-1)
        self.dungeonsanddragons.setObjectName("dungeonsanddragons")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(700, 490, 101, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/dungeons-dragons-d20-650954_1800x1800.webp"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.createcharacter = QtWidgets.QLabel(self.centralwidget)
        self.createcharacter.setGeometry(QtCore.QRect(210, 210, 281, 51))
        self.createcharacter.setMinimumSize(QtCore.QSize(0, 0))
        self.createcharacter.setBaseSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Harrington")
        font.setPointSize(20)
        font.setItalic(False)
        self.createcharacter.setFont(font)
        self.createcharacter.setObjectName("createcharacter")
        self.selectcharacter = QtWidgets.QLabel(self.centralwidget)
        self.selectcharacter.setFont(font)
        self.selectcharacter.setGeometry(QtCore.QRect(220, 290, 271, 51))
        self.selectcharacter.setBaseSize(QtCore.QSize(50, 50))
        self.selectcharacter.setObjectName("selectcharacter")
        self.vintage_paper = QtWidgets.QLabel(self.centralwidget)
        self.vintage_paper.setGeometry(QtCore.QRect(160, 190, 501, 181))
        self.vintage_paper.setText("")
        self.vintage_paper.setPixmap(QtGui.QPixmap("images/help-me-with-a-good-source-for-dnd-content-v0-956852t0m21b1.webp"))
        self.vintage_paper.setScaledContents(True)
        self.vintage_paper.setObjectName("vintage_paper")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(500, 230, 75, 23))
        self.create.setStyleSheet(
    """
    QPushButton {
        background-color: #A9845D; 
        color: white;
        border: 2px solid #5A2D0E;
        border-radius: 10px;
        padding: 100px 12px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #594031; 
    }
    QPushButton:pressed {
        background-color: #6B350B; 
    }
    """
)

        
        font = QtGui.QFont()
        font.setFamily("Harrington")
        font.setPointSize(12)
        self.create.setFont(font)
        self.create.setObjectName("create")
        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(500, 300, 75, 23))
        self.select.setStyleSheet(
    """
    QPushButton {
        background-color: #A9845D;
        color: white;
        border: 2px solid #5A2D0E;
        border-radius: 10px;
        padding: 100px 12px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #594031;
    }
    QPushButton:pressed {
        background-color: #6B350B; 
    }
    """
)
        
        font = QtGui.QFont()
        font.setFamily("Harrington")
        font.setPointSize(12)
        self.select.setFont(font)
        self.select.setObjectName("select")
        self.vintage_paper_2 = QtWidgets.QLabel(self.centralwidget)
        self.vintage_paper_2.setGeometry(QtCore.QRect(0, 0, 801, 700))
        self.vintage_paper_2.setText("")
        self.vintage_paper_2.setPixmap(QtGui.QPixmap("pngtree-dungeon-with-large-dragons-near-it-on-fire-picture-image_2875224.jpg"))
        self.vintage_paper_2.setScaledContents(True)
        self.vintage_paper_2.setObjectName("vintage_paper_2")
        self.vintage_paper_2.raise_()
        self.vintage_paper.raise_()
        self.dungeonsanddragons.raise_()
        self.logo.raise_()
        self.createcharacter.raise_()
        self.selectcharacter.raise_()
        self.create.raise_()
        self.select.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createcharacter.setText(_translate("MainWindow", "CREATE CHARACTER"))
        self.selectcharacter.setText(_translate("MainWindow", "SELECT CHARACTER"))
        self.create.setText(_translate("MainWindow", "create"))
        self.select.setText(_translate("MainWindow", "select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


