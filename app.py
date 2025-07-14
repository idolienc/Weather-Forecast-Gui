from PySide6 import QtWidgets, QtGui, QtCore
from dotenv import load_dotenv
import sys
import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather Forecast")

        self.city_input = QtWidgets.QLineEdit()
        self.city_input.setPlaceholderText("Enter city name...")
        self.city_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.go_button = QtWidgets.QPushButton("Go!")


        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.city_input)
        layout.addWidget(self.go_button)

        container = QtWidgets.QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.go_button.pressed.connect(self.get_weather)

    def get_weather(self):
        city = self.city_input.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        print(response.json())



app = QtWidgets.QApplication(sys.argv)

with open("style.qss", "r") as file:
    app.setStyleSheet(file.read())

window = MainWindow()
window.show()
app.exec()