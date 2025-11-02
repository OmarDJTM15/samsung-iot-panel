<!-- 🟦 Banner del Proyecto -->
<p align="center">
  <img src="https://i.ibb.co/ySTj8jX/iot-banner-samsung-style.png" width="800" alt="IoT Dashboard Banner">
</p>

<h1 align="center">🏠 Samsung IoT Data Logger</h1>
<p align="center">
  <b>Panel IoT profesional desarrollado en Python + Flet, con integración a Google Sheets.</b><br>
  Lectura de sensores en tiempo real, visualización gráfica, almacenamiento local y sincronización en la nube.
</p>

---

## 🚀 Características principales

- 🔌 **Comunicación serial** con Arduino / ESP32.  
- 💻 **Interfaz visual moderna** creada con Flet.  
- 🌡️ **Lectura en tiempo real** de sensores (temperatura, luz, humedad, etc.).  
- 📊 **Gráficos dinámicos** de datos en vivo.  
- 💾 **Registro local** en archivo CSV.  
- 📈 **Cálculo de estadísticas** (promedio, máximo, mínimo).  
- ☁️ **Exportación automática a Google Sheets** (almacenamiento en la nube).  

---

## 🧠 Tecnologías utilizadas

| Tecnología | Uso |
|-------------|-----|
| 🐍 **Python 3.12+** | Lenguaje principal |
| ⚙️ **Flet** | Interfaz gráfica multiplataforma |
| 🔌 **PySerial** | Comunicación serial con microcontrolador |
| 📈 **Pandas** | Análisis de datos y estadísticas |
| 🧰 **Gspread + OAuth2Client** | Integración con Google Sheets |
| 💾 **CSV** | Almacenamiento local de lecturas |

---

## 🧩 Estructura del proyecto

ProyectoIOT/
│
├── main.py # Interfaz Flet + lógica principal
├── device_manager.py # Comunicación con el dispositivo
├── requirements.txt # Dependencias del proyecto
├── .env # Variables locales (IGNORADO)
├── credentials.json # Credenciales de Google API (IGNORADO)
└── data/
└── sensor_log.csv # Registro de datos locales


---

## ⚙️ Instalación y configuración

### 1️⃣ Clona el repositorio
```bash
git clone https://github.com/OmarDJTM15/samsung-iot-panel.git
cd samsung-iot-panel

### 2️⃣ Crea el entorno virtual
python -m venv .venv
.\.venv\Scripts\activate

