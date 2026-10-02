FROM arm32v7/python:3.11-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyserial

WORKDIR /app

RUN git clone --depth 1 https://github.com/ole1986/centronic-py.git /app/centronic-py

COPY becker_test.py /app/becker_test.py

CMD ["python", "-u", "/app/becker_test.py"]
