import socket
import folium
from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)
locations = {}

def create_map(lat, lon, device_info, filename="app/templates/map.html"):
    map_ = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup=device_info).add_to(map_)
    map_.save(filename)

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/locations')
def get_locations():
    return jsonify(locations)

def main():
    host = '0.0.0.0'
    port = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print("الاستماع على المنفذ", port)

    while True:
        conn, addr = s.accept()
        print("اتصال من:", addr)

        data = conn.recv(1024).decode()
        print("مستلم:", data)

        if "Location:" in data:
            parts = data.split(", ")
            lat, lon = float(parts[1]), float(parts[2])
            device_info = parts[3].split(":")[1].strip()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            locations[addr] = {
                'lat': lat,
                'lon': lon,
                'device_info': device_info,
                'timestamp': timestamp
            }
            create_map(lat, lon, device_info)
            print(f"تم إنشاء الخريطة في الموقع: {lat}, {lon}")

            # عرض الرابط مع الاتجاهات
            map_link = f"https://www.google.com/maps/dir/?api=1&destination={lat},{lon}"
            print(f"رابط الخريطة: {map_link}")

        conn.close()

if __name__ == "__main__":
    from multiprocessing import Process
    server_process = Process(target=main)
    server_process.start()
    app.run(host='0.0.0.0', port=80)
