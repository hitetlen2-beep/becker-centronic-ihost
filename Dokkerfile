FROM arm32v7/python:3.11-slim

RUN pip install --no-cache-dir pyserial

WORKDIR /app

COPY becker_test.py /app/becker_test.py

CMD ["python", "-u", "/app/becker_test.py"]
