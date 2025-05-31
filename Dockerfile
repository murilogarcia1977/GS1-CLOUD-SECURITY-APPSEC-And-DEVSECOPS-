FROM python:3.12-slim

WORKDIR /app
COPY breach-checker.py .

RUN pip install requests

ENTRYPOINT ["python", "breach-checker.py"]
