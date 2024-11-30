import sys
from PyQt5.QtWidgets import QApplication
from guis import MainClass


def main() -> None:
    """Звпуск основного окна"""
    app = QApplication(sys.argv)
    main_window = MainClass()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
