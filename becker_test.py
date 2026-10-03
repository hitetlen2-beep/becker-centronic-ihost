import os
import subprocess
import time

DATA_DIR = "/data"
os.makedirs(DATA_DIR, exist_ok=True)

cmd = [
    "python",
    "-u",
    "/app/centronic-py/centronic-stick.py",
    "--device",
    "/dev/ttyACM0",
    "--send",
    "TRAIN",
    "--channel",
    "1:1",
]

print("=== Becker Centronic LILLA TRAIN ===", flush=True)
print("Persistent directory:", DATA_DIR, flush=True)
print("LIVE MODE: TRAIN parancs kuldese a Lilla redonyhoz.", flush=True)

result = subprocess.run(
    cmd,
    cwd=DATA_DIR,
    capture_output=True,
    text=True
)

print("--- STDOUT ---", flush=True)
print(result.stdout, flush=True)
print("--- STDERR ---", flush=True)
print(result.stderr, flush=True)
print("Exit code:", result.returncode, flush=True)

print("A teszt befejezodott. Varakozas...", flush=True)

while True:
    time.sleep(60)
