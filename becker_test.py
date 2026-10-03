import time
import serial

DEVICE = "/dev/ttyACM0"
BAUD = 115200

print("=== Becker Centronic command diagnostic ===", flush=True)
print("Device:", DEVICE, flush=True)
print("Baud:", BAUD, flush=True)
print("NINCS TRAIN / FEL / LE / STOP.", flush=True)

ser = serial.Serial(
    port=DEVICE,
    baudrate=BAUD,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

time.sleep(1)

def test(command, description):
    ser.reset_input_buffer()

    print("", flush=True)
    print("TEST:", description, flush=True)
    print("TX HEX:", command.hex(" "), flush=True)
    print("TX RAW:", repr(command), flush=True)

    ser.write(command)
    ser.flush()

    time.sleep(0.5)

    data = ser.read(512)

    print("RX HEX:", data.hex(" "), flush=True)
    print("RX RAW:", repr(data), flush=True)
    print(
        "RX TEXT:",
        data.decode("ascii", errors="replace"),
        flush=True
    )

tests = [
    (b"i", "INFO: i"),
    (b"i\r", "INFO: i + CR"),
    (b"i\r\n", "INFO: i + CRLF"),
    (b"r", "RSSI: r"),
    (b"r\r", "RSSI: r + CR"),
    (b"r\r\n", "RSSI: r + CRLF"),
]

for command, description in tests:
    test(command, description)
    time.sleep(0.5)

ser.close()

print("", flush=True)
print("=== Diagnostic finished ===", flush=True)

while True:
    time.sleep(60)
