from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class MainClass(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("GUI/gui.ui", self)
        self.setFixedSize(1271, 871)