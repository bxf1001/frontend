import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout

class PhoneBoothWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Phone Booth Portal")
        self.setGeometry(100, 100, 300, 150)  # Set window size and position

        # Create combo boxes
        self.combo_box1 = QComboBox(self)
        self.combo_box2 = QComboBox(self)

        # Populate combo box 1 with values from 1 to 12
        for i in range(1, 13):
            self.combo_box1.addItem(str(i))

        # Connect combo box 1 signal to update combo box 2
        self.combo_box1.currentIndexChanged.connect(self.update_combo_box2)

        # Create a label to display the selected minutes
        self.selected_minutes_label = QLabel(self)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box1)
        layout.addWidget(self.combo_box2)
        layout.addWidget(self.selected_minutes_label)
        self.setLayout(layout)

    def update_combo_box2(self):
        selected_value = int(self.combo_box1.currentText())
        remaining_values = [str(i) for i in range(1, 13) if i <= 12 - selected_value]
        self.combo_box2.clear()
        self.combo_box2.addItems(remaining_values)
        self.selected_minutes_label.setText(f"Selected minutes: {selected_value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhoneBoothWindow()
    window.show()
    sys.exit(app.exec_())
