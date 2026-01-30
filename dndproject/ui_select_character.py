
from PyQt5 import QtCore, QtGui, QtWidgets
from backend_select_character import CharacterSelectionManager
from ui_abilities import Ui_AbilitiesWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("font: bold 12pt 'Comic Sans MS';")
        MainWindow.resize(793, 700) 
        MainWindow.setStyleSheet("QMainWindow {"
                                 "background-image: url('images/e134dae41c4b437a8e81c0f8510690a5.jpg');"
                                 "background-repeat: no-repeat;"
                                 "background-position: center;"
                                 "}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")


        self.selectc_char_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setPointSize(12)
        font.setItalic(False)
        self.selectc_char_groupbox.setObjectName("selectc_char_groupbox")
        self.selectc_char_groupbox.setFont(font)
        self.selectc_char_groupbox.setStyleSheet("""
            QGroupBox#selectc_char_groupbox {
                border-image: url('images/360_F_604223671_RS327qPmIEjzubYMQz7oMVpGw7ROCo2S.jpg') 0 0 0 0 stretch stretch;
            }
        """)
        self.formLayout = QtWidgets.QFormLayout(self.selectc_char_groupbox)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setContentsMargins(10, 30, 10, 10)

        self.character_list = QtWidgets.QListWidget(self.selectc_char_groupbox)
        self.character_list.setObjectName("character_list")
        self.character_list.setStyleSheet("background-color: transparent; padding-top: 10px;")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.character_list)

        self.level_spinbox = QtWidgets.QSpinBox(self.selectc_char_groupbox)
        self.level_spinbox.setMinimum(1)
        self.level_spinbox.setMaximum(20)
        self.level_spinbox.setValue(1)
        self.level_spinbox.setPrefix("Level: ")
        self.level_spinbox.setObjectName("level_spinbox")
        self.level_spinbox.setStyleSheet("""
    QSpinBox {
        background-color: #A63117;
        color: white;
        border: 2px solid #5A2D0E;

        font-weight: bold;
        min-width: 80px;
    }

    QSpinBox::down-button {
        subcontrol-position: bottom right;
    }
    QSpinBox::up-arrow {

        width: 15px;
        height: 15px;
    }
    QSpinBox::down-arrow {
 
        width: 15px;
        height: 15px;
    }
""")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.level_spinbox)


        self.show_abilities_button = QtWidgets.QPushButton(self.selectc_char_groupbox)
        self.show_abilities_button.setText("Show Abilities")
        self.show_abilities_button.setObjectName("show_abilities_button")
        self.show_abilities_button.setStyleSheet(
    """
    QPushButton {
        background-color: #8C2C16; 
        color: white;
        border: 2px solid #5A2D0E;
        border-radius: 10px;
        padding: 5px 7px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #591C16; 
    }
    QPushButton:pressed {
        background-color: #6B350B; 
    }
    """)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.show_abilities_button)

        self.verticalLayout.addWidget(self.selectc_char_groupbox)


        self.character_stats_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.character_stats_groupbox.setObjectName("character_stats_groupbox")
        self.character_stats_groupbox.setFont(font)
        self.character_stats_groupbox.setStyleSheet("""
            QGroupBox#character_stats_groupbox {
                border-image: url('images/old-paper-with-opulent-ornament-borders-background-illustration-cartoon-style_976369-852.avif') 0 0 0 0 stretch stretch;
            }
        """)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.character_stats_groupbox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 30, 10, 10)

        self.select_char_texbox = QtWidgets.QTextEdit(self.character_stats_groupbox)
        self.select_char_texbox.setObjectName("select_char_texbox")
        self.select_char_texbox.setStyleSheet("background-color: transparent; padding-top: 10px;")
        self.select_char_texbox.setReadOnly(True)
        self.horizontalLayout_2.addWidget(self.select_char_texbox)
        self.verticalLayout.addWidget(self.character_stats_groupbox)

        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setObjectName("refresh_button")
        self.refresh_button.setStyleSheet(
    """
    QPushButton {
        background-color: #A69472; 
        color: white;
        border: 2px solid #5A2D0E;
        border-radius: 10px;
        padding: 5px 7px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #594031; 
    }
    QPushButton:pressed {
        background-color: #6B350B; 
    }
    """)
        self.verticalLayout.addWidget(self.refresh_button)

        self.backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.backbutton.setObjectName("backbutton")
        self.backbutton.setStyleSheet(
    """
    QPushButton {
        background-color: #F2A03D; 
        color: white;
        border: 2px solid #5A2D0E;
        border-radius: 10px;
        padding: 5px 7px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #A65132; 
    }
    QPushButton:pressed {
        background-color: #6B350B; 
    }
    """
)

        self.verticalLayout.addWidget(self.backbutton)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.character_manager = CharacterSelectionManager()


        self.character_list.itemClicked.connect(self.display_character)
        self.refresh_button.clicked.connect(self.load_characters_to_ui)
        self.show_abilities_button.clicked.connect(self.open_abilities_for_selected_character)


        self.load_characters_to_ui()

    def load_characters_to_ui(self):
        self.character_list.clear()
        characters_for_list = self.character_manager.load_characters()
        for char_id, char_name in characters_for_list:
            self.character_list.addItem(f"{char_name} (ID: {char_id})")

    def display_character(self, item):
        try:
            character_id_str = item.text().split('(ID: ')[1].strip(')')
            character_id = int(character_id_str)
        except (IndexError, ValueError):
            self.select_char_texbox.setText("Error: Could not parse character ID.")
            return
        
        details = self.character_manager.get_character_details(character_id)
        self.select_char_texbox.setText(details)

    def open_abilities_for_selected_character(self):
        selected_item = self.character_list.currentItem()
        if not selected_item:
            self.select_char_texbox.setText("Please select a character first.")
            return
        
        try:
            character_id_str = selected_item.text().split('(ID: ')[1].strip(')')
            character_id = int(character_id_str)
        except (IndexError, ValueError):
            self.select_char_texbox.setText("Error: Could not parse character ID.")
            return


        character = next((c for c in self.character_manager._characters_data if c['id'] == character_id), None)
        if not character:
            self.select_char_texbox.setText("Character data not found.")
            return
        

        level = self.level_spinbox.value()


        self.abilities_window = QtWidgets.QMainWindow()
        self.abilities_ui = Ui_AbilitiesWindow(character_class=character['char_class'])
        self.abilities_ui.setupUi(self.abilities_window)
        self.abilities_ui.update_abilities(level)
        self.abilities_window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Select Character"))
        self.selectc_char_groupbox.setTitle(_translate("MainWindow", "Select Character"))
        self.character_stats_groupbox.setTitle(_translate("MainWindow", "Character Stats"))
        self.backbutton.setText(_translate("MainWindow", "Back"))
        self.refresh_button.setText(_translate("MainWindow", "Refresh"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
