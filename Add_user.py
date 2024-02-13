import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
from qt_material import apply_stylesheet

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add User")
        self.setGeometry(100, 100, 300, 200)

        # Create input fields
        self.user_id_input = QLineEdit(self)
        self.value1_input = QLineEdit(self)
        self.value2_input = QLineEdit(self)
        self.value3_input = QLineEdit(self)

        # Create labels
        self.user_id_label = QLabel("User ID:", self)
        self.value1_label = QLabel("No1:", self)
        self.value2_label = QLabel("No2:", self)
        self.value3_label = QLabel("No3:", self)

        # Create submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.store_data)

        # Apply Material theme
        apply_stylesheet(app, theme='dark_teal.xml')

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.user_id_label)
        layout.addWidget(self.user_id_input)
        layout.addWidget(self.value1_label)
        layout.addWidget(self.value1_input)
        layout.addWidget(self.value2_label)
        layout.addWidget(self.value2_input)
        layout.addWidget(self.value3_label)
        layout.addWidget(self.value3_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def store_data(self):
        user_id = self.user_id_input.text()
        value1 = self.value1_input.text()
        value2 = self.value2_input.text()
        value3 = self.value3_input.text()

        try:
            with open('user_data.json', 'r') as f:
                user_data = json.load(f)
        except FileNotFoundError:
            user_data = {}

        if user_id in user_data:
            print("User already exists.")
        else:
            user_data[user_id] = {'1': value1, '2': value2, '3': value3}
            with open('user_data.json', 'w') as f:
                json.dump(user_data, f)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AnotherWindow()
    w.show()
    sys.exit(app.exec_())
