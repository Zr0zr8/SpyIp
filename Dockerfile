FROM python:3.9-slim

WORKDIR /app

# نقل ملفات المشروع
COPY . .

# تثبيت المكتبات المطلوبة
RUN apt-get update && \
    apt-get install -y binutils && \
    pip install --no-cache-dir -r requirements.txt

# تحويل البايلود إلى ملف تنفيذي
RUN pip install pyinstaller
RUN pyinstaller --onefile app/payload.py

# حقن البايلود في الصورة
RUN python app/inject_payload.py

# تشغيل السرفر
CMD ["gunicorn", "-c", "gunicorn_config.py", "app.server:app"]
