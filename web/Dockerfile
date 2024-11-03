FROM python:3.10.10

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

CMD ["waitress-serve", "--host=0.0.0.0", "--port=5480", "config.wsgi:application"]