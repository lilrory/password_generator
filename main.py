import random
import sys
import string

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 100)

        self.password_label = QLabel("Password:")
        self.password_label.setAlignment(Qt.AlignCenter)
        self.password_label.setFont(QFont('Arial', 16))

        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setFont(QFont('Arial', 18))

        self.generate_button = QPushButton("generate")
        self.generate_button.clicked.connect(self.generate_password)
        self.generate_button.setFont(QFont('Arial', 18))

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.password_label)
        main_layout.addWidget(self.password_display)
        main_layout.addWidget(self.generate_button)

        self.setLayout(main_layout)

    def generate_password(self):
        password_length = 12
        password_characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(password_characters) for i in range(password_length))
        self.password_display.setText(generated_password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    password_generator = PasswordGenerator()
    password_generator.show()
    sys.exit(app.exec_())
