from PyQt5 import QtCore, QtGui, QtWidgets
from backend_abilities import AbilitiesManager

class Ui_AbilitiesWindow(object):
    def __init__(self, character_class=""):
        super().__init__()
        self.character_class = character_class
        self.abilities_manager = AbilitiesManager()

    def setupUi(self, AbilitiesWindow):
        AbilitiesWindow.setObjectName("AbilitiesWindow")
        AbilitiesWindow.resize(400, 500)
        AbilitiesWindow.setStyleSheet("font: bold 12pt 'Comic Sans MS';")
        self.centralwidget = QtWidgets.QWidget(AbilitiesWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.vintage_paper_create_character = QtWidgets.QLabel(self.centralwidget)
        self.vintage_paper_create_character.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.vintage_paper_create_character.setPixmap(QtGui.QPixmap("images/e134dae41c4b437a8e81c0f8510690a5.jpg"))
        self.vintage_paper_create_character.setScaledContents(True)

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)

        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setText(f"{self.character_class} Abilities")
        self.verticalLayout.addWidget(self.titleLabel)

        self.abilitiesList = QtWidgets.QListWidget(self.centralwidget)
        self.abilitiesList.setObjectName("abilitiesList")
        self.abilitiesList.setStyleSheet("background-color: transparent; padding-top: 10px;")
        self.verticalLayout.addWidget(self.abilitiesList)
        

        AbilitiesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AbilitiesWindow)
        QtCore.QMetaObject.connectSlotsByName(AbilitiesWindow)

    def retranslateUi(self, AbilitiesWindow):
        _translate = QtCore.QCoreApplication.translate
        AbilitiesWindow.setWindowTitle(_translate("AbilitiesWindow", f"{self.character_class} Abilities"))

    def update_abilities(self, level):
       
        self.abilitiesList.clear()
        abilities = self.abilities_manager.get_abilities_by_class_and_level(self.character_class, level)
        for ability in abilities:
            item_text = f"{ability['name']}: {ability['description']}"
            self.abilitiesList.addItem(item_text)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AbilitiesWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())