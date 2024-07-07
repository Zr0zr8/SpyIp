FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# تشغيل سكربت الإعداد
RUN python scripts/setup.py

CMD ["gunicorn", "-c", "gunicorn_config.py", "app.server:app"]
