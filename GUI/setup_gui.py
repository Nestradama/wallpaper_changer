from PyQt6.QtWidgets import QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, \
    QInputDialog


class First_Setup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.source_combo_box = QComboBox(self)
        self.api_label = QLabel(self)
        self.api_user_input = QLineEdit(self)
        self.save_button = QPushButton("Save", self)
        self.save_button.setStyleSheet(
            """
            background-color: #262626;
            color: white;
            font-family: Titillium Web, sans-serif;
            font-size: 12px;
            """
        )
        self.main_window = None

        self.query_label = QLabel(self)
        self.query_input = QLineEdit(self)
        self.sort_type = QLabel(self)

        self.setup_ui()

    def save_bt_clicked(self):
        from settings import user_settings
        user_settings.User_Settings.set_user_settings(
            self.source_combo_box.currentText(),
            self.api_user_input.text(),
            self.query_input.text().lower()
        )
        self.close()

        from GUI.main_gui import normal_startup
        self.main_window = normal_startup()
        self.main_window.show()

    def setup_ui(self):
        self.setWindowTitle("User Settings")
        self.setGeometry(100, 100, 300, 200)

        self.source_combo_box.addItems(["Wallhaven", "Nasa"])
        self.source_combo_box.move(10, 40)
        self.source_combo_box.currentTextChanged.connect(self.combo_box_selection)
        self.source_combo_box.resize(100, 20)

        self.api_label.setText(f"Enter your {self.source_combo_box.currentText()} API keys:")
        self.api_label.move(10, 10)
        self.api_label.resize(280, 20)

        self.api_user_input.move(10, 70)
        self.api_user_input.resize(280, 20)
        self.api_user_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.api_user_input.setPlaceholderText("Enter your API key here")

        self.query_label.setText("Enter your query:")
        self.query_label.move(10, 130)
        self.query_label.resize(280, 20)
        self.query_input.move(10, 150)
        self.query_input.resize(280, 20)
        self.query_input.setPlaceholderText("Enter your query here")

        self.sort_type.setText("Sorting type: Random")
        self.sort_type.move(10, 170)
        self.sort_type.resize(280, 20)

        self.save_button.move(10, 100)
        self.save_button.clicked.connect(lambda: self.save_bt_clicked())

    def combo_box_selection(self):
        content = self.source_combo_box.currentText()
        self.api_label.setText(f"Enter your {content} API key:")

    @staticmethod
    def query_selection():
        inputdial = QInputDialog()
        inputdial.setLabelText("Enter your query:")
        inputdial.setWindowTitle("Query Selection")
        inputdial.setModal(True)
        inputdial.exec()
        settings.User_Settings.changer_user_settings(inputdial.textValue())
