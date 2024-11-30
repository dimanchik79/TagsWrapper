import json
import os.path

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QDialog
from tagssettings import TAGS, HELP


class Preview(QDialog):
    def __init__(self, html_text):
        super().__init__()
        self.html_text = html_text
        uic.loadUi("GUI/preview.ui", self)
        self.setFixedSize(1049, 898)
        self.preview.setHtml(self.html_text)


class Help(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/help.ui", self)
        self.setFixedSize(400, 400)
        self.help.setText(HELP['ENG'])
        self.btn_ru.clicked.connect(lambda: self.help.setText(HELP['RU']))
        self.btn_eng.clicked.connect(lambda: self.help.setText(HELP['ENG']))


class MainClass(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("GUI/gui.ui", self)
        self.setFixedSize(1271, 871)

        buttons = {'div': self.btn_div, 'span': self.btn_span, 'b': self.btn_b, 'i': self.btn_i, 'br': self.btn_br,
                   'hr': self.btn_hr, 'sup': self.btn_sup, 'sub': self.btn_sub, 'tleft': self.btn_tleft,
                   'tcenter': self.btn_tcenter, 'tjustify': self.btn_tjustify, 'tright': self.btn_tright,
                   'li': self.btn_li, 'th': self.btn_th, 'tr': self.btn_tr, 'td': self.btn_td, 'p': self.btn_p,
                   'ul': self.btn_ul, 'table': self.btn_table, 'ulli': self.btn_ulli
                   }

        if os.path.exists('settings.json'):
            with open('settings.json', 'r') as file:
                settings = json.load(file)
                self.t_dir.setText(settings['dir'])
                self.addstyle.setCheckState(settings['addstyle'])
                self.t_style.setText(settings['style'])
                self.textarea.setPlainText(settings['txt'])

        buttons["div"].clicked.connect(lambda: self.wrapped("div"))
        buttons["span"].clicked.connect(lambda: self.wrapped("span"))
        buttons["b"].clicked.connect(lambda: self.wrapped("b"))
        buttons["i"].clicked.connect(lambda: self.wrapped("i"))
        buttons["br"].clicked.connect(lambda: self.wrapped("br"))
        buttons["hr"].clicked.connect(lambda: self.wrapped("hr"))
        buttons["sub"].clicked.connect(lambda: self.wrapped("sub"))
        buttons["sup"].clicked.connect(lambda: self.wrapped("sup"))
        buttons["tleft"].clicked.connect(lambda: self.wrapped("tleft"))
        buttons["tcenter"].clicked.connect(lambda: self.wrapped("tcenter"))
        buttons["tjustify"].clicked.connect(lambda: self.wrapped("tjustify"))
        buttons["tright"].clicked.connect(lambda: self.wrapped("tright"))
        buttons["li"].clicked.connect(lambda: self.wrapped("li"))
        buttons["tr"].clicked.connect(lambda: self.wrapped("tr"))
        buttons["th"].clicked.connect(lambda: self.wrapped("th"))
        buttons["td"].clicked.connect(lambda: self.wrapped("td"))

        buttons["p"].clicked.connect(lambda: self.wrapped("p"))
        buttons["ul"].clicked.connect(lambda: self.wrapped("ul"))
        buttons["table"].clicked.connect(lambda: self.wrapped("table"))
        buttons["ulli"].clicked.connect(lambda: self.wrapped("ulli"))

        self.btn_paste.clicked.connect(self.paste_text)
        self.btn_clear.clicked.connect(self.clear_text)
        self.btn_dir.clicked.connect(self.change_directory)
        self.btn_preview.clicked.connect(self.preview)
        self.btn_undo.clicked.connect(lambda: self.comeback("undo"))
        self.btn_redo.clicked.connect(lambda: self.comeback("redo"))
        self.btn_help.clicked.connect(self.help)

        self.btn_stemp.clicked.connect(lambda: self.load_save_file("w"))
        self.btn_ltemp.clicked.connect(lambda: self.load_save_file("r"))
        self.btn_exit.clicked.connect(lambda: self.close())

    def closeEvent(self, event):
        settings = dict()
        settings['dir'] = self.t_dir.text()
        settings['addstyle'] = self.addstyle.isChecked()
        settings['style'] = self.t_style.text()
        settings['txt'] = self.textarea.toPlainText()
        with open('settings.json', 'w') as file:
            json.dump(settings, file)
        self.close()

    def wrapped(self, tag_name):
        text, new_text, style_text = '', '', ''
        cursor = self.textarea.textCursor()
        if self.addstyle.isChecked():
            if tag_name in ['ul']:
                style_text = f'{self.t_style.text()}'
            else:
                style_text = f' style="{self.t_style.text()}"' if self.addstyle.isChecked() else ''
        old_text = self.textarea.textCursor().selectedText()
        cursor.removeSelectedText()
        open_tag = TAGS[tag_name][0].replace('*style*', style_text)
        close_tag = TAGS[tag_name][1]
        if tag_name != "table":
            text_list = old_text.split("\u2029")
            for line in text_list:
                if line != '':
                    core_text = line[1:].strip() if (line[0] == "-" and tag_name == "ulli") else line.strip()
                else:
                    core_text = ''
                new_text += f"{open_tag}{core_text}{close_tag}\n"
            else:
                new_text = new_text[:-1]
                if tag_name == "ulli":
                    new_text = f"{TAGS['ul'][0].replace("*style*", style_text)}\n{new_text}\n{TAGS['ul'][1]}"
            cursor.insertText(new_text)
        else:
            cursor.insertText(f"{open_tag}{old_text}{close_tag}")
        self.textarea.setFocus()

    def paste_text(self):
        pos_cur = self.textarea.textCursor()
        pos_cur.insertText(QApplication.clipboard().text().strip())
        self.textarea.setFocus()

    def clear_text(self):
        reply = QMessageBox.question(self, "Внимание!!!", "Вы собираетесь удалить весь текст?",
                                     QMessageBox.Cancel | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.textarea.clear()
        self.textarea.setFocus()

    def comeback(self, vector):
        self.textarea.setFocus()
        if vector == "undo":
            self.textarea.undo()
            self.textarea.undo()
        if vector == "redo":
            self.textarea.redo()
            self.textarea.redo()

    def change_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select working directory")
        self.t_dir.setText(directory)
        self.textarea.setFocus()

    def preview(self):
        text = self.textarea.toPlainText()
        dialog = Preview(text)
        dialog.show()
        dialog.exec_()

    @staticmethod
    def help():
        dialog = Help()
        dialog.show()
        dialog.exec_()

    def file_exist(self, path, descriptor):
        self.textarea.setFocus()
        if self.t_dir.text() == "":
            QMessageBox.question(self, "Error!!!", "Select the work directory", QMessageBox.Ok)
            return False
        if path is False and descriptor == "r":
            QMessageBox.question(self, "Error!!!", "wrapped.txt not found!!!", QMessageBox.Ok)
            return False
        if descriptor == "w" or (path and descriptor == "r"):
            return True

    def load_save_file(self, descriptor):
        filename = self.t_dir.text() + "/wrapped.txt"
        path = os.path.exists(filename)
        if not self.file_exist(path, descriptor):
            return
        with open(filename, descriptor, encoding="utf-8") as file:
            if descriptor == "r":
                self.textarea.setPlainText(file.read())
            if descriptor == "w":
                file.write(self.textarea.toPlainText())
                QMessageBox.question(self, "Done!!!", "File wrapped.txt save to work directory", QMessageBox.Ok)
