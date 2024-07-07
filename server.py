import socket
import folium
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
locations = {}

def create_map(lat, lon, device_info, filename="templates/map.html"):
    map_ = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup=device_info).add_to(map_)
    map_.save(filename)

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/update')
def update():
    # تحديث الخريطة بآخر موقع
    if locations:
        latest_device = list(locations.keys())[-1]
        lat, lon, device_info = locations[latest_device]
        create_map(lat, lon, device_info)
    return redirect(url_for('index'))

def main():
    host = '0.0.0.0'
    port = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print("Listening on port", port)

    while True:
        conn, addr = s.accept()
        print("Connection from:", addr)

        data = conn.recv(1024).decode()
        print("Received:", data)

        if "Location:" in data:
            parts = data.split(", ")
            lat, lon = float(parts[1]), float(parts[2])
            device_info = parts[3].split(":")[1].strip()
            locations[addr] = (lat, lon, device_info)
            create_map(lat, lon, device_info)
            print(f"Map created at Location: {lat}, {lon}")

            # عرض الرابط مع الاتجاهات
            map_link = f"https://www.google.com/maps/dir/?api=1&destination={lat},{lon}"
            print(f"Map link: {map_link}")

        conn.close()

if __name__ == "__main__":
    from multiprocessing import Process
    server_process = Process(target=main)
    server_process.start()
    app.run(host='0.0.0.0', port=80)
