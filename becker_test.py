import os
import subprocess

DATA_DIR = "/data"
os.makedirs(DATA_DIR, exist_ok=True)

cmd = [
    "python",
    "-u",
    "/app/centronic-py/centronic-stick.py",
    "-t",
    "--device",
    "/dev/ttyACM0",
    "--send",
    "TRAIN",
    "--channel",
    "1:1",
]

print("=== Centronic-py PERSISTENT TEST MODE ===", flush=True)
print("Working directory:", DATA_DIR, flush=True)
print("A -t miatt NEM kuldunk adatot a Becker sticknek.", flush=True)

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

db_path = os.path.join(DATA_DIR, "centronic-stick.db")
print("Database exists:", os.path.exists(db_path), flush=True)
print("Database path:", db_path, flush=True)
print("Exit code:", result.returncode, flush=True)
