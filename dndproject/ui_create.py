from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from backend_create import class_base_stats, race_modifiers, CharacterManager 
from database import add_character 
from ui_weapons import Ui_MainWindow as WeaponsUI

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 738)
        MainWindow.setStyleSheet("font: bold 12pt 'Comic Sans MS';")
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(QtGui.QColor(117, 0, 0)))
        MainWindow.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vintage_paper_create_character = QtWidgets.QLabel(self.centralwidget)
        self.vintage_paper_create_character.setGeometry(QtCore.QRect(0, 0, 481, 800))
        self.vintage_paper_create_character.setPixmap(QtGui.QPixmap("images/e134dae41c4b437a8e81c0f8510690a5.jpg"))
        self.vintage_paper_create_character.setScaledContents(True)

        self.dnd_title_character_creatiion = QtWidgets.QLabel(self.centralwidget)
        self.dnd_title_character_creatiion.setGeometry(QtCore.QRect(110, 2, 321, 131))
        self.dnd_title_character_creatiion.setPixmap(QtGui.QPixmap("images/Dungeons-and-Dragons-Logo-2014.png"))
        self.dnd_title_character_creatiion.setScaledContents(True)

        self.dnd_logo_character_create = QtWidgets.QLabel(self.centralwidget)
        self.dnd_logo_character_create.setGeometry(QtCore.QRect(20, 13, 111, 101))
        self.dnd_logo_character_create.setPixmap(QtGui.QPixmap("images/dungeons-dragons-d20-650954_1800x1800.webp"))
        self.dnd_logo_character_create.setScaledContents(True)

        self.charactername_label = QtWidgets.QLabel("CHARACTER NAME", self.centralwidget)
        self.charactername_label.setGeometry(QtCore.QRect(50, 140, 191, 31))
        self.charactername_label.setFont(QtGui.QFont("Harrington", 14, QtGui.QFont.Bold))

        self.charactername_input = QtWidgets.QLineEdit(self.centralwidget)
        self.charactername_input.setGeometry(QtCore.QRect(50, 180, 251, 21))
        self.charactername_input.setStyleSheet("""
    QLineEdit {
        background-color: #A63117;
        color: white;
        border: 2px solid #5A2D0E;
        font-size: 15px;
        font-weight: bold;
        selection-color: white;
    }
""")

        self.race_label = QtWidgets.QLabel("Race:", self.centralwidget)
        self.race_label.setGeometry(QtCore.QRect(50, 230, 91, 16))

        self.race_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.race_combobox.setGeometry(QtCore.QRect(50, 280, 251, 22))
        self.race_combobox.addItems(race_modifiers.keys())
        self.race_combobox.currentIndexChanged.connect(self.load_base_stats)
        self.race_combobox.setStyleSheet("""
    QComboBox {
        background-color: #A63117; 
        color: white;
        border: 2px solid #5A2D0E;

        font-weight: bold;
    }
 
    QComboBox::down-arrow {
        width: 15px;
        height: 15px;
    }
    QComboBox QAbstractItemView {
        background-color: #A63117;
        border: 2px solid #5A2D0E;
        color: white;
        selection-background-color: #5A2D0E;
        selection-color: white;
        padding: 5px;
    }
""")


        self.class_label = QtWidgets.QLabel("Class:", self.centralwidget)
        self.class_label.setGeometry(QtCore.QRect(50, 330, 91, 16))

        self.class_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.class_combobox.setGeometry(QtCore.QRect(50, 370, 251, 22))
        self.class_combobox.addItems(class_base_stats.keys())
        self.class_combobox.currentIndexChanged.connect(self.load_base_stats)
        self.class_combobox.setStyleSheet("""
    QComboBox {
        background-color: #A63117; 
        color: white;
        border: 2px solid #5A2D0E;

        font-weight: bold;
    }
 
    QComboBox::down-arrow {
        width: 15px;
        height: 15px;
    }
    QComboBox QAbstractItemView {
        background-color: #A63117;
        border: 2px solid #5A2D0E;
        color: white;
        selection-background-color: #5A2D0E;
        selection-color: white;
        padding: 5px;
    }
""")



        self.stat_inputs = {}
        positions = {
            'strength': (60, 430), 'dexterity': (60, 470), 'constitution': (60, 500),
            'wisdom': (60, 530), 'intelligence': (60, 560), 'charisma': (60, 590)
        }

        for stat, (x, y) in positions.items():
            label = QtWidgets.QLabel(stat.capitalize(), self.centralwidget)
            label.setGeometry(QtCore.QRect(x, y, 91, 16))

            spinbox = QtWidgets.QSpinBox(self.centralwidget)
            spinbox.setGeometry(QtCore.QRect(x + 80, y, 81, 22))
            spinbox.setRange(0, 30)
            spinbox.valueChanged.connect(self.update_remaining_points)
            spinbox.setStyleSheet("""
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

            self.stat_inputs[stat] = spinbox

        self.remaining_label = QtWidgets.QLabel("Remaining Points: 8", self.centralwidget)
        self.remaining_label.setGeometry(QtCore.QRect(140, 620, 200, 20))

        self.weapons_button = QtWidgets.QPushButton("Weapons", self.centralwidget)
        self.weapons_button.setGeometry(QtCore.QRect(300, 490, 101, 61))
        self.weapons_button.clicked.connect(self.open_weapons_window)
        self.weapons_button.setStyleSheet(
    """
    QPushButton {
        background-color: #A63117; 
        color: white;
        border: 2px solid #5A2D0E;
        border-radius: 10px;
        padding: 100px 12px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #591C16; 
    }
    QPushButton:pressed {
        background-color: #6B350B; 
    }
    """
)


        self.back_button = QtWidgets.QPushButton("Back", self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(360, 650, 80, 40))
        self.back_button.setStyleSheet(
    """
    QPushButton {
        background-color: #F2A03D; 
        color: white;
        border: 2px solid #5A2D0E;
        border-radius: 10px;
        padding: 100px 12px;
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

        self.add_button = QtWidgets.QPushButton('Add Character', self.centralwidget)
        self.add_button.clicked.connect(self.add_character_to_db) 
        self.add_button.setGeometry(QtCore.QRect(50, 650, 200, 40))
        self.add_button.setStyleSheet(
    """
    QPushButton {
        background-color: #8C2C16; 
        color: white;
        border: 2px solid #5A2D0E;
        border-radius: 10px;
        padding: 100px 12px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #591C16; 
    }
    QPushButton:pressed {
        background-color: #6B350B; 
    }
    """
)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.character_manager = CharacterManager() 
        self.load_base_stats()

    def load_base_stats(self):
        selected_class = self.class_combobox.currentText()
        selected_race = self.race_combobox.currentText()

        calculated_stats = self.character_manager.calculate_base_stats(selected_class, selected_race)
        
        for stat, value in calculated_stats.items():
            self.stat_inputs[stat].setValue(value)

        self.character_manager.remaining_points = 8 
        self.remaining_label.setText(f'Remaining Points: {self.character_manager.remaining_points}')
        self.remaining_label.setStyleSheet("color: black")

    def update_remaining_points(self):
        selected_class = self.class_combobox.currentText()
        selected_race = self.race_combobox.currentText()
        current_stat_values = {stat: self.stat_inputs[stat].value() for stat in self.stat_inputs}

        self.character_manager.update_remaining_points(selected_class, selected_race, current_stat_values)
        
        if self.character_manager.remaining_points < 0:
            self.remaining_label.setText(f'Exceeded by {abs(self.character_manager.remaining_points)} points!')
            self.remaining_label.setStyleSheet("color: red")
        else:
            self.remaining_label.setText(f'Remaining Points: {self.character_manager.remaining_points}')
            self.remaining_label.setStyleSheet("color: black")

    def get_character_data(self):
        name = self.charactername_input.text().strip()
        race = self.race_combobox.currentText()
        char_class = self.class_combobox.currentText()
        level = 1  

        stats = {stat: self.stat_inputs[stat].value() for stat in self.stat_inputs}

        return {
            'name': name,
            'race': race,
            'char_class': char_class,
            'level': level,
            'stats': stats
        }

    def add_character_to_db(self):
        if self.character_manager.remaining_points < 0:
            QMessageBox.warning(None, 'Point Error', 'You have exceeded the available points.')
            return

        name = self.charactername_input.text().strip()
        if not name:
            QMessageBox.warning(None, 'Input Error', 'Please enter a character name.')
            return

        character_data = self.get_character_data()
        
        self.open_weapons_window(character_data)

    def open_weapons_window(self, character_data=None):
        selected_class = self.class_combobox.currentText()
        if not selected_class:
            QtWidgets.QMessageBox.warning(None, "No Class Selected", "Please select a class first.")
            return

        weapon_type_code = self.character_manager.get_weapon_type_for_class(selected_class)

        self.weapons_window = QtWidgets.QMainWindow()
        self.weapons_ui = WeaponsUI()
        self.weapons_ui.setupUi(self.weapons_window)

        self.weapons_ui.load_weapons(weapon_type_code)

        if character_data:
            self.weapons_ui.character_data = character_data
          


        self.weapons_window.show()

    def _final_add_character_to_db(self, character_data, selected_weapon_name):
        success = add_character(
            character_data['name'],
            character_data['race'],
            character_data['char_class'],
            character_data['level'],
            character_data['stats']['strength'],
            character_data['stats']['dexterity'],
            character_data['stats']['constitution'],
            character_data['stats']['wisdom'],
            character_data['stats']['intelligence'],
            character_data['stats']['charisma'],
            selected_weapon_name,
            self.character_manager.get_weapon_type_for_class(character_data['char_class']))
        
        if success:
            QMessageBox.information(None, 'Success', 'Character added successfully!')
            self.weapons_window.close() 
        else:
            QMessageBox.critical(None, 'Error', 'Failed to add character.')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())