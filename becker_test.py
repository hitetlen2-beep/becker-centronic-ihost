import sys
import time

sys.path.insert(0, "/app/becker-ha")

from pybecker.database import Database

DB_FILE = "/data/centronic-stick.db"

print("=== PYBECKER UNIT INIT TEST ===", flush=True)
print("Database:", DB_FILE, flush=True)
print("NINCS USB / RADIOADAS / TRAIN / FEL / LE / STOP.", flush=True)

try:
    db = Database(filename=DB_FILE)

    print("Database megnyitva.", flush=True)

    units_before = db.get_all_units()
    print("Configured units BEFORE:", repr(units_before), flush=True)

    if not units_before:
        print("Nincs configured unit -> init_dummy() indul.", flush=True)
        db.init_dummy()
    else:
        print("Mar van configured unit -> NEM inicializaljuk ujra.", flush=True)

    units_after = db.get_all_units()

    print("Configured units AFTER:", repr(units_after), flush=True)

    if units_after:
        print("SUCCESS: sajat pybecker unit rendelkezesre all.", flush=True)
        print("Unit:", repr(units_after[0]), flush=True)
    else:
        print("ERROR: tovabbra sincs configured unit.", flush=True)

    db.conn.close()

except Exception as error:
    print("ERROR:", repr(error), flush=True)

print("=== UNIT INIT TEST FINISHED ===", flush=True)

while True:
    time.sleep(60)
