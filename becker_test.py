import subprocess

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

print("=== Centronic-py TEST MODE ===", flush=True)
print("A -t miatt NEM kuldunk adatot a Becker sticknek.", flush=True)
print("Parancs generalasi teszt indul...", flush=True)

result = subprocess.run(cmd, capture_output=True, text=True)

print("--- STDOUT ---", flush=True)
print(result.stdout, flush=True)
print("--- STDERR ---", flush=True)
print(result.stderr, flush=True)
print("Exit code:", result.returncode, flush=True)
