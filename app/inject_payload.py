from stegano import lsb

def inject_payload(input_image, output_image, payload_file):
    with open(payload_file, "rb") as f:
        payload_content = f.read()
    
    # حقن البايلود في الصورة وحفظها
    encoded_image = lsb.hide(input_image, payload_content.decode('latin-1'))
    encoded_image.save(output_image)
    
    return output_image, "https://spyip.onrender.com/" + output_image.split('/')[-1]
