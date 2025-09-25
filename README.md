# 🗺️ NaviApp Kraków

**NaviApp Kraków** is a simple yet practical desktop application 🚗 that allows you to quickly plan car routes within Kraków.  
It combines the power of **PyQt5** (GUI), **Folium** (maps), and **OpenRouteService** (routing API).

---

## ✨ Features
- ✅ Select **start** and **destination** points
- ✅ Automatic location search (geopy)
- ✅ Display interactive map inside the application
- ✅ Fetch car routes from **OpenRouteService**
- ✅ Draw routes and points on the map using **Folium**

---

## 🛠️ Requirements
- Python **3.10+**
- Packages listed in `requirements.txt`

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the app
```bash
python main.py
```

---

## 📂 Project structure
```
navi_app/
├── main.py          # Application entry point
├── gui.py           # User interface (PyQt5)
├── map_utils.py     # Map handling and route drawing (Folium)
├── api_utils.py     # Fetching data from OpenRouteService API
├── requirements.txt # List of dependencies
└── README.md        # Project documentation
```

---

## 💻 Technologies used

- 🖥️ **PyQt5** – Application GUI
- 🌍 **PyQtWebEngine** – Embedding maps in the app
- 🗺️ **Folium** – Map generation
- 📍 **geopy** – Address geocoding
- 🌐 **requests** – API communication
- 🚦 **OpenRouteService** – Route calculation
- 🏞️ **OpenStreetMap** – Map data (ODbL)

---

## 📑 Data sources and licenses

Routes and maps provided by:
- **OpenRouteService**
- Geographic data: **OpenStreetMap** (ODbL – Open Database License)

---

## 📜 License

This project is available under the MIT license – see the LICENSE file.
