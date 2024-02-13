import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from qt_material import apply_stylesheet

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 600, 400)  # Set window size

        # Apply the Qt Material theme (choose a theme from the available options)
        apply_stylesheet(self, theme='dark_teal.xml')

        # Create buttons
        button_add_user = QPushButton("Add User", self)
        button_add_user.setGeometry(50, 50, 200, 40)

        button_connect_call = QPushButton("Connect Call", self)
        button_connect_call.setGeometry(50, 100, 200, 40)

        button_retrieve_data = QPushButton("Retrieve Data", self)
        button_retrieve_data.setGeometry(50, 150, 200, 40)

        button_about = QPushButton("About", self)
        button_about.setGeometry(50, 200, 200, 40)

        button_exit = QPushButton("Exit", self)
        button_exit.setGeometry(50, 250, 200, 40)
        button_exit.clicked.connect(self.close)  # Close the application when clicked

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
