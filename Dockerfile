FROM python:3.10-slim

ARG RUN_ID

ENV RUN_ID=${RUN_ID}

WORKDIR /app


RUN echo "Downloading model artifacts for Run ID: ${RUN_ID}" && \
    mkdir -p /app/model && \
    echo "${RUN_ID}" > /app/model/run_id.txt

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-c", "print('Model server starting for run:', open('/app/model/run_id.txt').read().strip())"]