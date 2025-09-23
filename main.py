from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
from geopy.geocoders import Nominatim
import sys

class NaviApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nawigacja Kraków")
        self.setGeometry(100, 100, 400, 200)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Pole startu
        layout.addWidget(QLabel("Punkt startowy:"))
        self.start_input = QLineEdit()
        layout.addWidget(self.start_input)

        # Pole mety
        layout.addWidget(QLabel("Punkt docelowy:"))
        self.end_input = QLineEdit()
        layout.addWidget(self.end_input)

        # Przycisk wyznacz trasę
        self.route_btn = QPushButton("Wyznacz trasę")
        self.route_btn.clicked.connect(self.show_coordinates)
        layout.addWidget(self.route_btn)

        self.setLayout(layout)

    def show_coordinates(self):
        geolocator = Nominatim(user_agent="nawigacja_krakow")
        start_place = self.start_input.text()
        end_place = self.end_input.text()

        try:
            start_loc = geolocator.geocode(f"{start_place}, Kraków")
            end_loc = geolocator.geocode(f"{end_place}, Kraków")

            if start_loc and end_loc:
                print(f"Start: {start_loc.latitude}, {start_loc.longitude}")
                print(f"Meta: {end_loc.latitude}, {end_loc.longitude}")
            else:
                print("Nie znaleziono jednego z miejsc.")
        except Exception as e:
            print("Błąd:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NaviApp()
    window.show()
    sys.exit(app.exec_())


from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Test PyQt5")
window.show()
sys.exit(app.exec_())
