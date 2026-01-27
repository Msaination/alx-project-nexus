FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "jobboard.wsgi:application", "--bind", "0.0.0.0:8000"]
