import flet as ft
from device_manager import DeviceManager

def main(page: ft.Page):
    page.title = "Samsung IoT Dashboard"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    device = DeviceManager()
    device.connect()

    data_display = ft.Text("Esperando datos del sensor...", size=20)
    status = ft.Text("Estado: conectado", size=14, color="green")

    def update_data(line):
        if line.startswith("TEMP:"):
            temp = line.replace("TEMP:", "")
            data_display.value = f"🌡 Temperatura: {temp} °C"
            page.update()

    def start(e):
        device.start_reading(update_data)
        status.value = "Leyendo datos..."
        page.update()

    def stop(e):
        device.stop_reading()
        status.value = "Lectura detenida"
        page.update()

    start_btn = ft.ElevatedButton("Iniciar lectura", on_click=start)
    stop_btn = ft.ElevatedButton("Detener", on_click=stop)

    page.add(
        ft.Column(
            [
                ft.Text("Panel IoT - Sensor de Temperatura", size=24, weight="bold"),
                data_display,
                ft.Row([start_btn, stop_btn], alignment=ft.MainAxisAlignment.CENTER),
                status,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
