from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from geopy.geocoders import Nominatim
import folium
import os
import sys

class NaviApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nawigacja Kraków")
        self.setGeometry(100, 100, 400, 200)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Punkt startowy:"))
        self.start_input = QLineEdit()
        layout.addWidget(self.start_input)

        layout.addWidget(QLabel("Punkt docelowy:"))
        self.end_input = QLineEdit()
        layout.addWidget(self.end_input)

        self.route_btn = QPushButton("Wyznacz trasę")
        self.route_btn.clicked.connect(self.show_map)
        layout.addWidget(self.route_btn)

        self.view = QWebEngineView()
        layout.addWidget(self.view)

        self.setLayout(layout)

    def show_map(self):
        geolocator = Nominatim(user_agent="nawigacja_krakow")
        start_place = self.start_input.text()
        end_place = self.end_input.text()

        try:
            start_loc = geolocator.geocode(f"{start_place}, Kraków")
            end_loc = geolocator.geocode(f"{end_place}, Kraków")

            if start_loc and end_loc:
                # Środek mapy jako średnia współrzędnych
                center_lat = (start_loc.latitude + end_loc.latitude) / 2
                center_lon = (start_loc.longitude + end_loc.longitude) / 2
                mapa = folium.Map(location=[center_lat, center_lon], zoom_start=14)
                folium.Marker([start_loc.latitude, start_loc.longitude], tooltip="Start").add_to(mapa)
                folium.Marker([end_loc.latitude, end_loc.longitude], tooltip="Meta").add_to(mapa)

                map_file = os.path.abspath("mapa.html")
                mapa.save(map_file)
                self.view.load(QUrl.fromLocalFile(map_file))
            else:
                print("Nie znaleziono jednego z miejsc.")
        except Exception as e:
            print("Błąd:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NaviApp()
    window.show()
    sys.exit(app.exec_())