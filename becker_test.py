import sys
import time

# A friss Becker projekt pybecker mappaja
sys.path.insert(0, "/app/becker-ha")

from pybecker.becker_helper import BeckerCommunicator

DEVICE = "/dev/ttyACM0"

print("=== PYBECKER RX ONLY TEST ===", flush=True)
print("Device:", DEVICE, flush=True)
print("Friss BeckerCommunicator hasznalata.", flush=True)
print("CSAK VETEL - nincs send(), TRAIN, FEL, LE vagy STOP.", flush=True)


def received(match):
    try:
        packet = match.group(0)

        print("", flush=True)
        print("=== RECEIVED PACKET ===", flush=True)
        print("RAW:", repr(packet), flush=True)
        print("HEX:", packet.hex(" "), flush=True)

        try:
            print("TEXT:", packet.decode("ascii", errors="replace"), flush=True)
        except Exception as error:
            print("Decode error:", repr(error), flush=True)

    except Exception as error:
        print("Callback error:", repr(error), flush=True)


try:
    communicator = BeckerCommunicator(
        device=DEVICE,
        callback=received
    )

    communicator.start()

    print("BeckerCommunicator elindult.", flush=True)
    print("Varakozas Centronic radio telegramokra...", flush=True)

    while communicator.is_alive():
        time.sleep(1)

    print("ERROR: BeckerCommunicator leallt.", flush=True)

except Exception as error:
    print("ERROR:", repr(error), flush=True)

while True:
    time.sleep(60)
