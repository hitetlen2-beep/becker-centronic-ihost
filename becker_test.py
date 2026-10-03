import sys
import os
import time

sys.path.insert(0, "/app/becker-ha")

from pybecker.database import Database

DATA_DIR = "/data"
DB_FILE = "/data/centronic-stick.db"

print("=== PYBECKER PERSISTENT DATABASE TEST ===", flush=True)
print("NINCS RADIOADAS / TRAIN / FEL / LE / STOP.", flush=True)

os.makedirs(DATA_DIR, exist_ok=True)

print("Database path:", DB_FILE, flush=True)
print("Database existed before:", os.path.exists(DB_FILE), flush=True)

try:
    db = Database(filename=DB_FILE)

    print("SUCCESS: pybecker database megnyitva.", flush=True)
    print("Database exists now:", os.path.exists(DB_FILE), flush=True)

    if os.path.exists(DB_FILE):
        print("Database size:", os.path.getsize(DB_FILE), "bytes", flush=True)

    # Lezarjuk az adatbazis-kapcsolatot.
    if hasattr(db, "conn"):
        db.conn.close()

    print("SUCCESS: database teszt befejezve.", flush=True)

except Exception as error:
    print("ERROR:", repr(error), flush=True)

while True:
    time.sleep(60)
