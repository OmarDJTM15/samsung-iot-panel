import flet as ft
from device_manager import DeviceManager

def main(page: ft.Page):
    page.title = "Samsung IoT Control Panel"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    device = DeviceManager()
    device.connect()

    status = ft.Text("Estado: Esperando comandos...", size=16)

    def send_on(e):
        response = device.send_command("ON")
        status.value = response
        page.update()

    def send_off(e):
        response = device.send_command("OFF")
        status.value = response
        page.update()

    btn_on = ft.ElevatedButton("Encender 💡", on_click=send_on)
    btn_off = ft.ElevatedButton("Apagar 🌙", on_click=send_off)

    page.add(
        ft.Column(
            [
                ft.Text("Control de Dispositivo IoT", size=24, weight="bold"),
                ft.Row([btn_on, btn_off], alignment=ft.MainAxisAlignment.CENTER),
                status
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
