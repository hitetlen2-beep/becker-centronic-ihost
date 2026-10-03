import subprocess
import time

print("=== Becker Centronic LISTEN TEST ===", flush=True)
print("CSAK VETEL - nincs TRAIN es nincs radioadas.", flush=True)
print("Centronic-py listen mode, /dev/ttyACM0, 115200 baud", flush=True)

cmd = [
    "python",
    "-u",
    "/app/centronic-py/centronic-stick.py",
    "--listen",
    "--device",
    "/dev/ttyACM0",
]

process = subprocess.Popen(
    cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1
)

for line in process.stdout:
    print(line.rstrip(), flush=True)

print("Listen process ended. Exit code:", process.wait(), flush=True)

while True:
    time.sleep(60)
