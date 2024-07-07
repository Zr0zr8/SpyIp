from stegano import lsb

def inject_payload(input_image, output_image, payload_file):
    with open(payload_file, "rb") as f:
        payload_content = f.read()
    
    lsb.hide(input_image, payload_content.decode('latin-1')).save(output_image)
    return output_image
