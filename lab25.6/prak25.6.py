from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QFileDialog,
)


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Налаштування вікна
        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 800, 600)

        # Створення віджету тексту
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # Створення меню
        menuBar = self.menuBar()

        # Файл
        fileMenu = menuBar.addMenu("File")

        # Дії для меню
        newAction = QAction("New", self)
        openAction = QAction("Open", self)
        saveAction = QAction("Save", self)
        quitAction = QAction("Quit", self)

        # Підключення функцій
        newAction.triggered.connect(self.newFile)
        openAction.triggered.connect(self.openFile)
        saveAction.triggered.connect(self.saveFile)
        quitAction.triggered.connect(self.close)

        # Додавання дій до меню
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(quitAction)

    def newFile(self):
        """Створює новий файл."""
        self.textEdit.clear()

    def openFile(self):
        """Відкриває існуючий файл."""
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options
        )
        if fileName:
            with open(fileName, "r", encoding="utf-8") as file:
                self.textEdit.setText(file.read())

    def saveFile(self):
        """Зберігає файл."""
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options
        )
        if fileName:
            with open(fileName, "w", encoding="utf-8") as file:
                file.write(self.textEdit.toPlainText())


def main():
    app = QApplication([])
    editor = TextEditor()
    editor.show()
    app.exec()


if __name__ == "__main__":
    main()
