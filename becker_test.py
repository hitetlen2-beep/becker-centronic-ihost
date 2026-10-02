import os
import sys
import time
import serial

DEVICE = "/dev/ttyACM0"

print("=== Becker Centronic iHost diagnostic ===", flush=True)
print("UID:", os.getuid(), flush=True)
print("Device:", DEVICE, flush=True)

if not os.path.exists(DEVICE):
    print("ERROR: /dev/ttyACM0 nem talalhato.", flush=True)
    sys.exit(1)

print("SUCCESS: /dev/ttyACM0 megtalalva.", flush=True)

try:
    ser = serial.Serial(DEVICE, 57600, timeout=1)
except Exception as error:
    print("ERROR:", error, flush=True)
    sys.exit(2)

print("SUCCESS: Becker port megnyitva 57600 8N1.", flush=True)
print("TESZT MOD: nem kuldunk adatot a sticknek.", flush=True)

while True:
    print("Becker diagnostic running - port open.", flush=True)
    time.sleep(30)
