FROM python:3.7
RUN mkdir /app

COPY api /app/api
COPY static /app/static
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

WORKDIR /app/api
EXPOSE 5000
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
