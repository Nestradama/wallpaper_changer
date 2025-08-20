from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QMainWindow, QLabel, QHBoxLayout, QPushButton, QComboBox

import issue_handler
from functions.gui_functions import GUIFunctions
from settings import user_settings as settings
from functions import gui_functions
from GUI import main_gui


class Edit_Settings:
    def __init__(self):
        super().__init__()

    @staticmethod
    def settings_popup(window_instance=None):
        original_widget = window_instance.takeCentralWidget() #Transfers ownership to keep widget alive

        settings_widget = QWidget()

        save_button = QPushButton("Save", settings_widget)
        sorting_type_combobox = QComboBox()
        sorting_type_combobox.addItems(
            ["Random", "Recently added", "Top-rated today", "Top-rated last 3 days", "Top-rated this week",
             "Top-rated this month", "Top-rated this year"])

        purity_combobox = QComboBox()
        purity_combobox.addItems(["sfw","sketchy", "nsfw"])

        user_data = settings.User_Settings.retrieve_user_settings()
        user_wallhaven_api_key = user_data['API_KEYS']['wallhaven']
        user_query = user_data['API_SETTINGS']['query']
        user_source = user_data['API_SETTINGS']['source']
        user_sorting = user_data['API_SETTINGS']['sorting']
        user_resolution = user_data['API_SETTINGS']['resolution']
        user_purity = user_data['API_SETTINGS']['purity']

        Edit_Settings.combobox_set_text(sorting_type_combobox, user_sorting)
        Edit_Settings.combobox_set_text(purity_combobox, user_purity)

        for i, sorting_type in enumerate(
                sorting_type_combobox.itemText(i) for i in range(sorting_type_combobox.count())):
            print(sorting_type)
            print(user_sorting)
            if str(sorting_type).lower() == str(user_sorting).lower():
                sorting_type_combobox.setCurrentIndex(i)
                print("match")
                break
            else:
                print("no match")
                sorting_type_combobox.setCurrentIndex(0)

        settings_editing = {
            "wallhaven_api_key": QLineEdit(user_wallhaven_api_key),
            "query": QLineEdit(user_query),
            "source": QLineEdit(user_source),
            "sorting": sorting_type_combobox,
            "resolution": QLineEdit(user_resolution),
            "purity": purity_combobox
        }

        settings_qlabels = {
            "wallhaven_api_key": QLabel("Enter your wallhaven API key:"),
            "query": QLabel("Enter your query:"),
            "source": QLabel("Enter your source:"),
            "sorting": QLabel("Enter your sorting type:"),
            "resolution": QLabel("Enter your screen resolution:"),
            "purity": QLabel("SFW or NSFW?:")
        }

        vertical_layout = QVBoxLayout()

        for key, value in settings_editing.items():
            horizontal_layout = QHBoxLayout()
            horizontal_layout.addWidget(settings_qlabels[key])
            horizontal_layout.addWidget(value)
            vertical_layout.addLayout(horizontal_layout)

        vertical_layout.addWidget(save_button)

        settings_widget.setLayout(vertical_layout)
        settings_widget.settings_qlines = settings_editing
        print("GGWP2")
        window_instance.setCentralWidget(settings_widget)
        save_button.clicked.connect(
            lambda: Edit_Settings.save_bt_clicked(settings_widget, window_instance, original_widget))

    @staticmethod
    def save_bt_clicked(settings_widget, window_instance=None, original_widget=None):
        gui_functions.GUIFunctions.agglomerate_data(settings_widget.settings_qlines)
        window_instance.setCentralWidget(original_widget)#Put back original widget as central widget
        window_instance.show()
        window_instance.adjustSize()
        settings_widget.close()

    @staticmethod
    def combobox_set_text(combobox, user_setting):

        for i, combobox_item  in enumerate(
                combobox.itemText(i) for i in range(combobox.count())):
            print(combobox_item)
            print(user_setting)
            if str(combobox_item).lower() == str(user_setting).lower():
                combobox.setCurrentIndex(i)
                print("match")
                break
            else:
                print("no match")
                combobox.setCurrentIndex(0)