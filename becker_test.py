import os
import sys
import time
import serial

DEVICE = "/dev/ttyACM0"

print("=== Becker Centronic RX monitor ===", flush=True)
print("UID:", os.getuid(), flush=True)
print("Device:", DEVICE, flush=True)

if not os.path.exists(DEVICE):
    print("ERROR: /dev/ttyACM0 nem talalhato.", flush=True)
    sys.exit(1)

try:
    ser = serial.Serial(DEVICE, 57600, timeout=0.2)
except Exception as error:
    print("ERROR:", error, flush=True)
    sys.exit(2)

print("SUCCESS: Becker port megnyitva 57600 8N1.", flush=True)
print("RX ONLY: a program NEM kuld adatot.", flush=True)
print("Varakozas a sticktol erkezo adatokra...", flush=True)

last_status = time.time()

while True:
    data = ser.read(256)

    if data:
        print("RX HEX:", data.hex(" "), flush=True)
        print("RX RAW:", repr(data), flush=True)

    if time.time() - last_status >= 30:
        print("RX monitor running...", flush=True)
        last_status = time.time()
