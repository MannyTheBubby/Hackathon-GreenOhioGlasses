from PyQt6.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acc Window")
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()
        label = QLabel("Hello, World!")
        layout.addWidget(label)
        self.setLayout(layout)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()
        label = QLabel("Hello, World!")
        layout.addWidget(label)
        self.setLayout(layout)

def main():
    app = QApplication([])
    window = MainWindow()

    label = QLabel(window)
    label.setText("Hello, World!")
    # label.setFont('Arial', 20)

    loginWindow = LoginWindow()
    loginWindow.show()
    
    window.show()
    app.exec()

if __name__ == "__main__":
    main()