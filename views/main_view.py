"""" This module contains the main view for the application. """
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class MainView(QWidget):
    """" This module contains the main view for the application. """

    def __init__(self):
        super().__init__()

        self.welcome_label = QLabel("Welcome to the main page!")

        layout = QVBoxLayout()
        layout.addWidget(self.welcome_label)

        self.setLayout(layout)
