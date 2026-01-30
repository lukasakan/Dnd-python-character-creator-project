from PyQt5 import QtCore, QtGui, QtWidgets
from backend_weapons import get_weapons_by_type, confirm_weapon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("font: bold 12pt 'Comic Sans MS';")
        MainWindow.resize(478, 738)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vintage_paper = QtWidgets.QLabel(self.centralwidget)
        self.vintage_paper.setGeometry(QtCore.QRect(6, -8, 471, 721))
        self.vintage_paper.setPixmap(QtGui.QPixmap("images/e134dae41c4b437a8e81c0f8510690a5.jpg"))
        self.vintage_paper.setScaledContents(True)

        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox1.setGeometry(QtCore.QRect(330, 120, 120, 20))
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(330, 300, 120, 20))
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(330, 480, 120, 20))

        for cb in [self.checkBox1, self.checkBox_2, self.checkBox_3]:
            cb.stateChanged.connect(lambda _, c=cb: self.handle_exclusive_checkbox(c) if c.isChecked() else None)

        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(340, 620, 75, 23))
        self.back_button.setStyleSheet(self.button_style())
        self.back_button.setText("Back")
        self.back_button.clicked.connect(self.back_to_create)
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

        self.confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_button.setGeometry(QtCore.QRect(70, 620, 75, 23))
        self.confirm_button.setStyleSheet(self.button_style())
        self.confirm_button.setText("Confirm")
        self.confirm_button.clicked.connect(self.confirm_weapon_selection)
        self.confirm_button.setStyleSheet(
    """
    QPushButton {
        background-color: #8C2C16; 
        color: white;
        border: 2px solid #5A2D0E;
        border-radius: 10px;
        padding: 100px 6px;
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

        self.wep_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.wep_label_1.setGeometry(QtCore.QRect(80, 60, 201, 131))
        self.wep_label_1.setScaledContents(True)

        self.wep_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.wep_label_2.setGeometry(QtCore.QRect(70, 240, 201, 131))
        self.wep_label_2.setScaledContents(True)

        self.wep_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.wep_label_3.setGeometry(QtCore.QRect(70, 430, 201, 131))
        self.wep_label_3.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.character_data = None

    def button_style(self):
        return '''
            QPushButton {
                background-image: url("images/4807.jpg");
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
                color:white;
                border: 2px solid #563d2d;
            }
        '''

    def handle_exclusive_checkbox(self, checked_box):
        for cb in [self.checkBox1, self.checkBox_2, self.checkBox_3]:
            if cb is not checked_box:
                cb.setChecked(False)

    def back_to_create(self):
        self.confirm_button.window().close()

    def load_weapons(self, weapon_type):
        weapons = get_weapons_by_type(weapon_type)
        labels = [self.wep_label_1, self.wep_label_2, self.wep_label_3]
        checkboxes = [self.checkBox1, self.checkBox_2, self.checkBox_3]

        for i in range(len(weapons)):
            name, img_path = weapons[i]
            pixmap = QtGui.QPixmap(img_path)
            labels[i].setPixmap(pixmap)
            checkboxes[i].setText(name)

    def confirm_weapon_selection(self):
        selected_weapon = None
        for checkbox in [self.checkBox1, self.checkBox_2, self.checkBox_3]:
            if checkbox.isChecked():
                selected_weapon = checkbox.text()
                break

        if not selected_weapon:
            QtWidgets.QMessageBox.warning(None, "No Weapon Selected", "Please select a weapon before confirming.")
            return

        success, message = confirm_weapon(self.character_data, selected_weapon)
        if success:
            QtWidgets.QMessageBox.information(None, "Success", message)
            self.confirm_button.window().close()
        else:
            QtWidgets.QMessageBox.critical(None, "Error", message)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


