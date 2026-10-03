import time
import serial

DEVICE = "/dev/ttyACM0"
BAUD = 115200

print("=== Becker Centronic USB diagnostic ===", flush=True)
print("Device:", DEVICE, flush=True)
print("Baud:", BAUD, flush=True)
print("NINCS TRAIN / FEL / LE / STOP parancs.", flush=True)

ser = serial.Serial(
    port=DEVICE,
    baudrate=BAUD,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=2
)

time.sleep(1)
ser.reset_input_buffer()

def query(command, name):
    print("", flush=True)
    print("QUERY:", name, flush=True)

    ser.reset_input_buffer()
    ser.write(command)
    ser.flush()

    time.sleep(1)

    data = ser.read(512)

    print("RX HEX:", data.hex(" "), flush=True)
    print("RX RAW:", repr(data), flush=True)

    try:
        print("RX TEXT:", data.decode("ascii", errors="replace"), flush=True)
    except Exception as error:
        print("Decode error:", error, flush=True)

# Stick information
query(b"i", "INFO (i)")

# Radio/RSSI information
query(b"r", "RSSI (r)")

print("", flush=True)
print("Diagnostic finished.", flush=True)

ser.close()

while True:
    time.sleep(60)
