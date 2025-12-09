import serial
import time
import os
from datetime import datetime
import subprocess

# Configure serial port
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

LOG_FILE = #Path

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

try:
    log(f"Opening serial port: {ser.portstr}")

    if ser.is_open:
        log("Serial port opened successfully.")

        while True:
            line = ser.readline()
            if line:
                decoded_line = line.decode('utf-8').strip()
                #log(f"Received: {decoded_line}")

                if decoded_line == "NOTEPAD_MACRO":
                    #log("Macro Clicked")
                    subprocess.Popen(
                        [r"C:\Program Files\Notepad++\notepad++.exe"],
                        creationflags=subprocess.CREATE_NO_WINDOW
                    )

            time.sleep(0.1)

    else:
        log("Failed to open serial port.")

except serial.SerialException as e:
    log(f"Serial port error: {e}")
except Exception as e:
    log(f"Unexpected error: {e}")
finally:
    if ser.is_open:
        ser.close()
        log("Serial port closed.")

