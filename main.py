import flet as ft
from device_manager import DeviceManager
from collections import deque
import pandas as pd
import csv
from datetime import datetime

def main(page: ft.Page):
    page.title = "Samsung IoT Data Logger"
    page.theme_mode = "dark"

    device = DeviceManager()
    device.connect()

    temps = deque(maxlen=100)
    lights = deque(maxlen=100)
    log_file = "data/sensor_log.csv"

    # Crear archivo CSV si no existe
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["timestamp", "temperature", "light"])

    data_display = ft.Text("Esperando datos del sensor...", size=16)
    stats_display = ft.Text("Estadísticas: -", size=14, color="cyan")
    status = ft.Text("Estado: Esperando...", size=14)

    def save_data(temp, light):
        """Guarda una nueva línea en el archivo CSV"""
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp, light])

    def update_data(line):
        if "TEMP:" in line and "LIGHT:" in line:
            try:
                parts = line.split(";")
                temp = float(parts[0].split(":")[1])
                light = float(parts[1].split(":")[1])

                temps.append(temp)
                lights.append(light)
                save_data(temp, light)

                data_display.value = f"🌡 {temp:.1f} °C | 💡 {light:.1f} %"
                page.update()
            except Exception as e:
                data_display.value = f"Error: {e}"
                page.update()

    def calc_stats(e):
        """Calcula estadísticas usando pandas"""
        try:
            df = pd.read_csv(log_file)
            avg_temp = df["temperature"].mean()
            avg_light = df["light"].mean()
            min_temp = df["temperature"].min()
            max_temp = df["temperature"].max()
            stats_display.value = (
                f"📊 Promedios — Temp: {avg_temp:.1f}°C, Luz: {avg_light:.1f}%\n"
                f"🔺 Máx: {max_temp:.1f}°C | 🔻 Mín: {min_temp:.1f}°C"
            )
            page.update()
        except Exception as e:
            stats_display.value = f"⚠️ Error al calcular estadísticas: {e}"
            page.update()

    def start(e):
        device.start_reading(update_data)
        status.value = "Leyendo y registrando datos..."
        page.update()

    def stop(e):
        device.stop_reading()
        status.value = "Lectura detenida."
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("📁 IoT Data Logger", size=24, weight="bold"),
                data_display,
                ft.Row([
                    ft.ElevatedButton("Iniciar", on_click=start),
                    ft.ElevatedButton("Detener", on_click=stop),
                    ft.ElevatedButton("Calcular estadísticas", on_click=calc_stats)
                ], alignment="center"),
                stats_display,
                status
            ],
            alignment="center",
            horizontal_alignment="center",
        )
    )

ft.app(target=main)
