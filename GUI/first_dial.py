from PyQt6.QtWidgets import QMessageBox

from GUI.setup_gui import First_Setup
# Library Imports
import sys
from PyQt6.QtWidgets import QApplication

# Self-imports
from settings.user_settings import User_Settings


class Program_Setup:
    def __init__(self):
        pass

    @staticmethod
    def is_first_launch():

        msg_box = QMessageBox()

        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setText("Is this your first time launching the program? (I might be wrong, just asking)")
        msg_box.setInformativeText("If you are, you will have to enter your NASA and Wallhaven API keys.")
        msg_box.setWindowTitle("Welcome!")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)
        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Yes:
            Program_Setup.first_launch_setup_gui()
        else:
            print("I didn't do this")

    @staticmethod
    def first_launch_setup_gui():
        app = QApplication(sys.argv)
        main = First_Setup()
        main.show()
        sys.exit(app.exec())
