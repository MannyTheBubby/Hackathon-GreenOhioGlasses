from PyQt6.QtWidgets import *

def main():
    app = QApplication([])
    window = QWidget()

    label = QLabel(window)
    label.setText("Hello, World!")
    # label.setFont('Arial', 20)
    
    window.show()
    app.exec()

if __name__ == "__main__":
    main()