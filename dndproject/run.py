import sys
from PyQt5 import QtCore, QtGui, QtWidgets


from ui_main import Ui_MainWindow as Ui_MainPage
from ui_create import Ui_MainWindow as Ui_CreatePage
from ui_select_character import Ui_MainWindow as Ui_SelectCharacterPage

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)


        self.main_page = QtWidgets.QMainWindow()
        self.ui_main = Ui_MainPage()
        self.ui_main.setupUi(self.main_page)
        self.stacked_widget.addWidget(self.main_page)

        self.main_page_size = QtCore.QSize(800, 600)


        self.create_character_page = QtWidgets.QMainWindow()
        self.ui_create = Ui_CreatePage()
        self.ui_create.setupUi(self.create_character_page)
        self.stacked_widget.addWidget(self.create_character_page)

        self.create_page_size = QtCore.QSize(478, 738)


        self.select_character_page = QtWidgets.QMainWindow()
        self.ui_select = Ui_SelectCharacterPage()
        self.ui_select.setupUi(self.select_character_page)
        self.stacked_widget.addWidget(self.select_character_page)

        self.select_page_size = QtCore.QSize(793, 613)

        self.init_ui()

    def init_ui(self):

        self.ui_main.create.clicked.connect(self.show_create_character_page)
        self.ui_main.select.clicked.connect(self.show_select_character_page)


        self.ui_create.back_button.clicked.connect(self.show_main_page)
        self.ui_select.backbutton.clicked.connect(self.show_main_page)


        self.show_main_page()

    def show_main_page(self):
        self.stacked_widget.setCurrentWidget(self.main_page)
        self.resize(self.main_page_size)

    def show_create_character_page(self):
        self.stacked_widget.setCurrentWidget(self.create_character_page)
        self.resize(self.create_page_size)

    def show_select_character_page(self):
        self.stacked_widget.setCurrentWidget(self.select_character_page)
        self.resize(self.select_page_size)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationWindow()
    window.show()
    sys.exit(app.exec_())
