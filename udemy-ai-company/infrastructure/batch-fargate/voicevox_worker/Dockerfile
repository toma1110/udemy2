FROM voicevox/voicevox_engine:cpu-latest

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-pip \
    && python3 -m pip install --break-system-packages --no-cache-dir boto3 requests \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY voicevox_worker.py /app/voicevox_worker.py

ENTRYPOINT ["python3", "/app/voicevox_worker.py"]
