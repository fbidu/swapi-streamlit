FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py /app

ENTRYPOINT [ "python", "main.py" ]