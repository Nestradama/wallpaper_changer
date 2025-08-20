# Library Imports
import os
import sys
import time
import PyQt6.QtWidgets
from PyQt6.QtWidgets import QApplication

# Self-imports
from settings.user_settings import User_Settings
from GUI import main_gui, first_dial


def main():
    app = QApplication(sys.argv)  # Ensures that GUI can run anytime

    print(os.getcwd())

    with open("C:/Users/Corentin/PycharmProjects/PythonProject3/style.qss", "r") as file:
        _style = file.read()
        app.setStyleSheet(_style)

    check_first_launch = User_Settings.check_first_launch()

    print("Check", check_first_launch)
    if not check_first_launch:
        main_gui.normal_startup.user_query_gui()
    else:
        print("I went here")
        first_dial.Program_Setup.is_first_launch()


# os.remove("config.ini")
main()
