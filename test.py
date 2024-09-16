from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QMainWindow


class DialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialog Window')
        layout = QVBoxLayout()
        self.setLayout(layout)

        accept_button = QPushButton('Accept', self)
        accept_button.clicked.connect(self.accept)
        layout.addWidget(accept_button)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')


if __name__ == '__main__':
    app = QApplication([])

    dialog = DialogWindow()
    print(dialog.exec())
    if dialog.exec() == QDialog.DialogCode.Accepted:
        print('ee')
        main_window = MainWindow()
        main_window.show()

