
import sys
from PyQt5.QtWidgets import QApplication
from models import DB, engine

from GUI.guis import MainClass


def main() -> None:
    """Звпуск основного окна"""
    app = QApplication(sys.argv)
    main_window = MainClass()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    DB.metadata.create_all(engine)
    main()
