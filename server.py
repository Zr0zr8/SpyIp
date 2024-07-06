import socket
import folium
from flask import Flask, render_template

app = Flask(__name__)

def create_map(lat, lon, filename="templates/map.html"):
    map_ = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup='Target Location').add_to(map_)
    map_.save(filename)

@app.route('/')
def index():
    return render_template('map.html')

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
            lat, lon = data.split(":")[1].strip().split(", ")
            create_map(float(lat), float(lon))
            print(f"Map created at Location: {lat}, {lon}")

        conn.close()

if __name__ == "__main__":
    from multiprocessing import Process
    server_process = Process(target=main)
    server_process.start()
    app.run(host='0.0.0.0', port=80)
