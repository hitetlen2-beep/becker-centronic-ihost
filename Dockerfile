FROM arm32v7/python:3.11-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyserial

WORKDIR /app

# Regi centronic-py - megtartjuk osszehasonlitashoz
RUN git clone --depth 1 \
    https://github.com/ole1986/centronic-py.git \
    /app/centronic-py

# Frissebb Becker / pybecker implementacio
RUN git clone --depth 1 \
    https://github.com/RainerStaude/hass-becker-component-plus-pybecker.git \
    /app/becker-ha

COPY becker_test.py /app/becker_test.py

CMD ["python", "-u", "/app/becker_test.py"]
