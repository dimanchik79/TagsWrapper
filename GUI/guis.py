import json
from os import path

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from models import DB, engine
from tagssettings import TAGS

class MainClass(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        DB.metadata.create_all(engine)
        uic.loadUi("GUI/gui.ui", self)
        self.setFixedSize(1271, 871)

        buttons = (self.btn_div,self.btn_span, self.btn_b, self.btn_i, self.btn_br, self.btn_hr, self.btn_sup,
                   self.btn_sub, self.btn_tleft, self.btn_tcenter, self.btn_tjustify, self.btn_tright, self.btn_li,
                   self.btn_th, self.btn_tr, self.btn_td, self.btn_p, self.btn_ul, self.btn_table)

        if path.exists('temp.json'):
            with open('temp.json', 'r') as file:
                temp = json.load(file)

        buttons[0].clicked.connect(lambda: self.wrapped(0))
        buttons[1].clicked.connect(lambda: self.wrapped(1))
        buttons[2].clicked.connect(lambda: self.wrapped(2))
        buttons[3].clicked.connect(lambda: self.wrapped(3))
        buttons[4].clicked.connect(lambda: self.wrapped(4))
        buttons[5].clicked.connect(lambda: self.wrapped(5))
        buttons[6].clicked.connect(lambda: self.wrapped(6))
        buttons[7].clicked.connect(lambda: self.wrapped(7))
        buttons[8].clicked.connect(lambda: self.wrapped(8))
        buttons[9].clicked.connect(lambda: self.wrapped(9))
        buttons[10].clicked.connect(lambda: self.wrapped(10))
        buttons[11].clicked.connect(lambda: self.wrapped(11))
        buttons[12].clicked.connect(lambda: self.wrapped(12))
        buttons[13].clicked.connect(lambda: self.wrapped(13))
        buttons[14].clicked.connect(lambda: self.wrapped(14))
        buttons[15].clicked.connect(lambda: self.wrapped(15))

        buttons[16].clicked.connect(lambda: self.wrapped(16))
        buttons[17].clicked.connect(lambda: self.wrapped(17))
        buttons[18].clicked.connect(lambda: self.wrapped(18))

        self.btn_paste.clicked.connect(self.paste_text)
        self.btn_clear.clicked.connect(self.clear_text)

        self.textarea.textChanged.connect(self.on_text_changed)

    def wrapped(self, tag_count):
        style_text = f' style="{self.t_style.text()}"' if self.addstyle.isChecked() else ''
        open_tag = TAGS[tag_count][0].replace('*style*', style_text)
        close_tag = TAGS[tag_count][1]
        old_text = self.textarea.textCursor().selectedText()
        cursor = self.textarea.textCursor()
        cursor.removeSelectedText()
        cursor.insertText(f"{open_tag}{old_text}{close_tag}")
        self.textarea.setFocus()

    def paste_text(self):
        pos_cur = self.textarea.textCursor()
        pos_cur.insertText(QApplication.clipboard().text())
        self.textarea.setFocus()

    def clear_text(self):
        reply = QMessageBox.question(self, "Внимание!!!", "Вы собираетесь удалить весь текст?",
                                     QMessageBox.Cancel | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.textarea.clear()

    def on_text_changed(self):
        pass