FROM python:3.11.9-bullseye

COPY requirements.txt /requirements.txt
COPY api /app
COPY mh_forecast /mh_forecast
COPY models /models
COPY setup.py /setup.py
COPY MANIFEST.in /MANIFEST.in
COPY .env /.env

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn app.fast:app --host 0.0.0.0 --port $PORT
