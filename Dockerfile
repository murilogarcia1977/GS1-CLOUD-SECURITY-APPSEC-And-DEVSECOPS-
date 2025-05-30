
FROM python:3.11-slim

WORKDIR /app

COPY check_vazamentos.py .

RUN pip install --no-cache-dir requests

CMD ["python", "check_vazamentos.py"]
