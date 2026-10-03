import sys
import asyncio
import time

sys.path.insert(0, "/app/becker-ha")

from pybecker.becker import Becker

DEVICE = "/dev/ttyACM0"
DB_FILE = "/data/centronic-stick.db"
CHANNEL = "1:1"

print("=== LILLA REDONY - STOP TEST ===", flush=True)
print("Device:", DEVICE, flush=True)
print("Database:", DB_FILE, flush=True)
print("Channel:", CHANNEL, flush=True)
print("NORMAL HALT/STOP parancs - NINCS TRAIN.", flush=True)


async def main():
    becker = None

    try:
        becker = Becker(
            device_name=DEVICE,
            init_dummy=False,
            db_filename=DB_FILE
        )

        print("Pybecker elindult.", flush=True)
        print("STOP/HALT kuldese...", flush=True)

        await becker.send(CHANNEL, "HALT")

        print("STOP/HALT elkuldve.", flush=True)

        # Hagyunk idot a communicatornak a kikuldesre.
        await asyncio.sleep(2)

    except Exception as error:
        print("ERROR:", repr(error), flush=True)

    finally:
        if becker is not None:
            try:
                becker.close()
            except Exception as error:
                print("Close error:", repr(error), flush=True)

        print("STOP teszt befejezve.", flush=True)


asyncio.run(main())

while True:
    time.sleep(60)
