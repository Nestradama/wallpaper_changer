import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout, QWidget

from GUI import gui_edit_settings as edit_settings
from functions import gui_functions
from settings import user_settings as settings


class normal_startup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = None
        self.query_label = None
        self.user_input = None
        self.save_button = None
        self.settings_button = None
        self.change_wallpaper_button = None

        self.build_widget()
        # self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("User Settings")
        self.setGeometry(100, 100, 100, 100)
        self.setCentralWidget(self.main_widget)

    def build_widget(self):

        layout_vertical = QVBoxLayout()
        layout_horizontal = QHBoxLayout()

        self.query_label = QLabel("Enter your query: ")
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Enter your query here")

        self.save_button = QPushButton("Save")
        self.settings_button = QPushButton("Settings")
        self.change_wallpaper_button = QPushButton("Change wallpaper")

        layout_vertical.addWidget(self.query_label)
        layout_vertical.addWidget(self.user_input)
        layout_vertical.addLayout(layout_horizontal)

        layout_horizontal.addWidget(self.save_button)
        layout_horizontal.addWidget(self.settings_button)
        layout_horizontal.addWidget(self.change_wallpaper_button)
        self.main_widget = QWidget()
        self.main_widget.setLayout(layout_vertical)

        self.save_button.clicked.connect(self.save_bt_clicked)

        self.settings_button.move(10, 100)
        self.settings_button.clicked.connect(self.sett_bt_clicked)

        self.change_wallpaper_button.move(10, 130)
        self.change_wallpaper_button.clicked.connect(self.change_wallpaper_clicked)

    def sett_bt_clicked(self):
        edit_settings.Edit_Settings.settings_popup(window_instance=self)
        self.user_input.clear()

    def change_wallpaper_clicked(self):
        gui_functions.GUIFunctions.change_wallpaper(self.user_input.text())
        self.user_input.clear()

    def save_bt_clicked(self):
        settings.User_Settings.changer_user_settings(self.user_input.text())
        self.user_input.clear()

    @staticmethod
    def user_query_gui():
        app = QApplication(sys.argv)
        main = normal_startup()
        main.show()
        sys.exit(app.exec())


class MainContentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.main_widget = None
        self.build_widget()
