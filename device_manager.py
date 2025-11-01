import serial
import time
from dotenv import load_dotenv
from pathlib import Path
import os
import threading

class DeviceManager:
    def __init__(self):
        env_path = Path(__file__).parent / ".env"
        load_dotenv(dotenv_path=env_path)
        self.port = os.getenv("PORT")
        self.baud_rate = int(os.getenv("BAUD_RATE"))
        self.device = None
        self.running = False
        self.data_callback = None  # función que recibirá los datos

    def connect(self):
        try:
            self.device = serial.Serial(self.port, self.baud_rate, timeout=1)
            time.sleep(2)
            print("✅ Dispositivo conectado correctamente.")
        except Exception as e:
            print(f"❌ Error de conexión: {e}")

    def start_reading(self, callback):
        """Lee datos del dispositivo continuamente en un hilo aparte"""
        if not self.device:
            print("⚠️ No hay dispositivo conectado.")
            return
        
        self.running = True
        self.data_callback = callback
        threading.Thread(target=self._read_loop, daemon=True).start()

    def _read_loop(self):
        while self.running:
            if self.device.in_waiting > 0:
                line = self.device.readline().decode().strip()
                if self.data_callback:
                    self.data_callback(line)
            time.sleep(0.5)

    def stop_reading(self):
        self.running = False

    def close(self):
        if self.device:
            self.device.close()
            print("🔌 Conexión cerrada.")
