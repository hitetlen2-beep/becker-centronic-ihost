import sys
import time

sys.path.insert(0, "/app/becker-ha")

from pybecker.becker_helper import BeckerCommunicator

DEVICE = "/dev/ttyACM0"

print("=== PYBECKER RX DECODE TEST ===", flush=True)
print("Device:", DEVICE, flush=True)
print("CSAK VETEL - nincs send(), TRAIN, FEL, LE vagy STOP.", flush=True)


def received(match):
    try:
        packet = match.group(0)

        print("", flush=True)
        print("=== RECEIVED PACKET ===", flush=True)
        print("RAW:", repr(packet), flush=True)
        print("HEX:", packet.hex(" "), flush=True)

        print("unit_id:", match.group("unit_id"), flush=True)
        print("channel:", match.group("channel"), flush=True)
        print("command:", match.group("command"), flush=True)
        print("argument:", match.group("argument"), flush=True)

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
