import os
import sys
import time
import serial

DEVICE = "/dev/ttyACM0"

print("=== Becker Centronic iHost diagnostic ===", flush=True)
print(f"Python: {sys.version}", flush=True)
print(f"UID: {os.getuid()}", flush=True)
print(f"Device: {DEVICE}", flush=True)

if not os.path.exists(DEVICE):
print(f"ERROR: {DEVICE} nem talalhato.", flush=True)
sys.exit(1)

st = os.stat(DEVICE)
print(
f"Device found. UID={st.st_uid}, GID={st.st_gid}, "
f"mode={oct(st.st_mode & 0o777)}",
flush=True,
)

try:
ser = serial.Serial(
port=DEVICE,
baudrate=57600,
bytesize=serial.EIGHTBITS,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
timeout=1,
write_timeout=1,
)

print("SUCCESS: /dev/ttyACM0 megnyitva 57600 8N1 beallitassal.", flush=True)
print("NEM kuldunk adatot a Becker sticknek.", flush=True)

except Exception as exc:
print(f"ERROR opening serial port: {type(exc).__name__}: {exc}", flush=True)
sys.exit(2)

try:
while True:
time.sleep(30)
print("Becker diagnostic running - port open.", flush=True)
finally:
ser.close()
