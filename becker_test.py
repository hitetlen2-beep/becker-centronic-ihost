import sys
import asyncio
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

sys.path.insert(0, "/app/becker-ha")

from pybecker.becker import Becker

DEVICE = "/dev/ttyACM0"
DB_FILE = "/data/centronic-stick.db"
LILLA_CHANNEL = "1:1"
PORT = 8080


class BeckerBridge:
    def __init__(self):
        self.loop = asyncio.new_event_loop()

        self.becker = Becker(
            device_name=DEVICE,
            init_dummy=False,
            db_filename=DB_FILE
        )

        self.thread = threading.Thread(
            target=self._run_loop,
            daemon=True
        )
        self.thread.start()

    def _run_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def send(self, command):
        future = asyncio.run_coroutine_threadsafe(
            self.becker.send(LILLA_CHANNEL, command),
            self.loop
        )

        # Megvarjuk, hogy a pybecker atvegye/kikuldje a parancsot.
        future.result(timeout=10)


bridge = BeckerBridge()


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = urlparse(self.path).path.lower()

        try:
            if path == "/lilla/up":
                bridge.send("UP")
                message = "Lilla UP OK"

            elif path == "/lilla/stop":
                bridge.send("HALT")
                message = "Lilla STOP OK"

            elif path == "/lilla/down":
                bridge.send("DOWN")
                message = "Lilla DOWN OK"

            elif path == "/health":
                message = "Becker Bridge OK"

            else:
                self.send_response(404)
                self.end_headers()
                return

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(message.encode())

        except Exception as error:
            print("COMMAND ERROR:", repr(error), flush=True)

            self.send_response(500)
            self.end_headers()
            self.wfile.write(repr(error).encode())

    def log_message(self, format, *args):
        print(format % args, flush=True)


print("=== BECKER iHOST BRIDGE ===", flush=True)
print("Device:", DEVICE, flush=True)
print("Database:", DB_FILE, flush=True)
print("Lilla:", LILLA_CHANNEL, flush=True)
print("HTTP port:", PORT, flush=True)

server = HTTPServer(("0.0.0.0", PORT), Handler)

print("Bridge running.", flush=True)
print("/lilla/up", flush=True)
print("/lilla/stop", flush=True)
print("/lilla/down", flush=True)
print("/health", flush=True)

server.serve_forever()
