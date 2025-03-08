from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acc Window")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()
        label = QLabel("Hello, World!")
        layout.addWidget(label)
        self.setLayout(layout)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 600, 400)

        layout = QHBoxLayout()
        label = QLabel("Login")
        layout.addWidget(label)
        self.setLayout(layout)


def main():
    app = QApplication([])
    window = MainWindow()
    # window.show()

    loginWindow = LoginWindow()
    loginWindow.show()
    
    
    app.exec()

if __name__ == "__main__":
    main()