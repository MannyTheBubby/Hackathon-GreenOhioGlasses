from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from server import encrypt_file, receive_file
from cli import decrypt_file

window = None

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acc Window")
        self.setGeometry(100, 100, 400, 300)

        # masterLayout = QHBoxLayout()
        mainWin = QVBoxLayout()

        #-----------------Action Section-----------------
        actionSection = QHBoxLayout()

        sendButton = QPushButton("Send")
        sendButton.clicked.connect(self.send)

        ConnectButton = QPushButton("Connect")
        ConnectButton.clicked.connect(self.recive)
         
        actionSection.addWidget(sendButton)
        actionSection.addWidget(ConnectButton)
        #-----------------Action Section-----------------

        #----------------History Section-----------------

        historyButton = QPushButton("History")
        historyButton.clicked.connect(self.history)

        

        #----------------History Section-----------------        

        mainWin.addLayout(actionSection)
        mainWin.addWidget(historyButton)
        self.setLayout(mainWin)

    def send(self):
        None
    
    def recive(self):
        None

    def history(self): 
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
    #loginWindow.show()
    
    
    app.exec()

if __name__ == "__main__":
    main()