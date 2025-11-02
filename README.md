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

2️⃣ Crea el entorno virtual
python -m venv .venv
.\.venv\Scripts\activate
2️⃣ Crea el entorno virtual
python -m venv .venv
.\.venv\Scripts\activate

3️⃣ Instala las dependencias
pip install -r requirements.txt
```
---

###4️⃣ Configura tu archivo .env
Crea un archivo .env en la raíz:

PORT=COM3
BAUD_RATE=115200
(Ajusta el puerto según tu sistema operativo.)

---

###5️⃣ Configura credenciales de Google Sheets
Crea un proyecto en Google Cloud Console.

1. Activa las APIs:
2. Google Sheets API
3. Google Drive API
4. Crea una Service Account y descarga credentials.json.
5. Coloca ese archivo en la raíz del proyecto.
6. Comparte tu hoja de Google con el correo de la cuenta de servicio.
   
---

###🧠 Uso del programa

1. Conecta tu dispositivo (ESP32 o Arduino).
2. Ejecuta el programa:
```bash
  python main.py
```
3. En la interfaz podrás:
  Iniciar / detener la lectura de datos.
  Ver lecturas gráficas en tiempo real.
  Calcular estadísticas.
  Exportar los datos a Google Sheets.

---

###📸 Capturas de pantalla
<p align="center"> <img src="https://i.ibb.co/5BgMQhC/iot-dashboard-example.png" width="700" alt="IoT Dashboard Screenshot"> </p>

---

###🔒 Seguridad

El proyecto no incluye credenciales ni datos personales.
Asegúrate de mantener fuera del repositorio:

```bash
.env
credentials.json
```
---

###🧑‍💻 Autor

Omar de Jesús
Desarrollador IoT en formación
Proyecto guiado por mentoría Samsung Developer Path

<p align="center"> <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"> <img src="https://img.shields.io/badge/Python-Flet-blue?style=for-the-badge&logo=python"> </p> 

---

###🪪 Licencia
Este proyecto se distribuye bajo la licencia MIT, lo que permite su uso libre con atribución.

---

###🌟 Agradecimientos
  
  A la comunidad de Flet y Python IoT.
  A los recursos educativos de Google Cloud Developers.
  Y a todos los mentores que promueven el aprendizaje práctico y profesional.
