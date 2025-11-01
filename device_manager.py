import serial
import time
from dotenv import load_dotenv
import os

from pathlib import Path
env_path = Path(__file__).parent / ".env"


class DeviceManager:
    def __init__(self):
        load_dotenv(dotenv_path=env_path)
        self.port = os.getenv("PORT")
        self.baud_rate = int(os.getenv("BAUD_RATE"))
        self.device = None

    def connect(self):
        try:
            self.device = serial.Serial(self.port, self.baud_rate, timeout=1)
            time.sleep(2)
            print("✅ Dispositivo conectado correctamente.")
        except Exception as e:
            print(f"❌ Error de conexión: {e}")

    def send_command(self, command):
        if self.device:
            self.device.write((command + "\n").encode())
            time.sleep(0.5)
            response = self.device.readline().decode().strip()
            return response
        else:
            return "❌ Dispositivo no conectado."

    def close(self):
        if self.device:
            self.device.close()
            print("🔌 Conexión cerrada.")
