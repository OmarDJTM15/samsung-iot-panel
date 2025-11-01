import flet as ft
from device_manager import DeviceManager
from collections import deque

def main(page: ft.Page):
    page.title = "Samsung IoT Dashboard"
    page.theme_mode = "dark"

    device = DeviceManager()
    device.connect()

    # Guardar últimas lecturas (máximo 20)
    temps = deque(maxlen=20)
    lights = deque(maxlen=20)

    temp_chart = ft.LineChart(
        tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLACK),
        width=600,
        height=300,
        expand=True,
        min_y=0,
        max_y=100,
        border=ft.border.all(1, ft.Colors.WHITE10),
        left_axis=ft.ChartAxis(labels_size=40, title=ft.Text("Temperatura °C")),
        bottom_axis=ft.ChartAxis(labels_size=20),
        data_series=[
            ft.LineChartData(
                data_points=[],
                color=ft.Colors.AMBER,
                curved=True,
                stroke_width=3
            ),
        ],
    )

    light_chart = ft.LineChart(
        tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLACK),
        width=600,
        height=300,
        expand=True,
        min_y=0,
        max_y=100,
        border=ft.border.all(1, ft.Colors.WHITE10),
        left_axis=ft.ChartAxis(labels_size=40, title=ft.Text("Luz %")),
        bottom_axis=ft.ChartAxis(labels_size=20),
        data_series=[
            ft.LineChartData(
                data_points=[],
                color=ft.Colors.CYAN,
                curved=True,
                stroke_width=3
            ),
        ],
    )

    status = ft.Text("Estado: Esperando datos...", size=14)

    def update_data(line):
        if "TEMP:" in line and "LIGHT:" in line:
            try:
                parts = line.split(";")
                temp = float(parts[0].split(":")[1])
                light = float(parts[1].split(":")[1])

                temps.append(temp)
                lights.append(light)

                # Actualizar gráficos
                temp_chart.data_series[0].data_points = [
                    ft.LineChartDataPoint(i, t) for i, t in enumerate(temps)
                ]
                light_chart.data_series[0].data_points = [
                    ft.LineChartDataPoint(i, l) for i, l in enumerate(lights)
                ]

                status.value = f"🌡 {temp:.1f} °C | 💡 {light:.1f} %"
                page.update()
            except Exception as e:
                status.value = f"Error de lectura: {e}"
                page.update()

    def start(e):
        device.start_reading(update_data)
        status.value = "Leyendo datos..."
        page.update()

    def stop(e):
        device.stop_reading()
        status.value = "Lectura detenida"
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("Panel IoT – Sensores en tiempo real", size=24, weight="bold"),
                ft.Row([ft.ElevatedButton("Iniciar", on_click=start),
                        ft.ElevatedButton("Detener", on_click=stop)], alignment="center"),
                temp_chart,
                light_chart,
                status
            ],
            alignment="center",
            horizontal_alignment="center",
            scroll=ft.ScrollMode.ALWAYS
        )
    )

ft.app(target=main)
