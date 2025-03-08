from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

window = None

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acc Window")
        self.setGeometry(100, 100, 400, 300)

        # masterLayout = QHBoxLayout()

        mainWin = QVBoxLayout()
        actionSection = QHBoxLayout()

        sendButton = QPushButton("Send")
        sendButton.clicked.connect(self.send)

        ReciveButton = QPushButton("Recive")
        ReciveButton.clicked.connect(self.recive)

        
        
        label = QLabel("Hello, World!")
        label1 = QLabel("Hello, World!")

        layout = QVBoxLayout()

        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addStretch(100)

        mainWin.addLayout(actionSection)
        self.setLayout(mainWin)

    def send(self):
        None
    
    def recive(self):
        None

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 600, 400)

        dlgLayout = QVBoxLayout()
        
        layout = QFormLayout()
        layout.setVerticalSpacing(20)
        layout.addRow("Username", QLineEdit())
        layout.addRow("Password", QLineEdit())

        button = QPushButton("Login")
        button.clicked.connect(self.login)
        # button1 = QPushButton("signup")
        # button1.clicked.connect(self.signUp)
        
        dlgLayout.addLayout(layout)
        dlgLayout.addWidget(button)
        self.setLayout(dlgLayout)

    def login(self):
        None

    def signUP(self):
        None


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()

    loginWindow = LoginWindow()
    # loginWindow.show()
    
    
    app.exec()

if __name__ == "__main__":
    main()