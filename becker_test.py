import os
import time

TEST_FILE = "/data/becker-persistence-test.txt"

print("=== Becker persistent volume test ===", flush=True)

if os.path.exists(TEST_FILE):
    print("SUCCESS: a korabbi tesztfajl megmaradt.", flush=True)
    with open(TEST_FILE, "r") as f:
        print("Tartalom:", f.read(), flush=True)
else:
    print("Elso futas: tesztfajl letrehozasa...", flush=True)
    with open(TEST_FILE, "w") as f:
        f.write("becker-data OK")
    print("SUCCESS: tesztfajl letrehozva.", flush=True)

print("Path:", TEST_FILE, flush=True)

while True:
    time.sleep(60)
