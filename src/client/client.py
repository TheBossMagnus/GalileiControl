import socket
import time
import get_data

server_addr = "2C:CF:67:99:D4:0E"
port = 3

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    print(f"Connecting to server {server_addr}...")
    s.connect((server_addr, port))
    print("Connected successfully")

    while True:
        time.sleep(5)
        message = f"User: {get_data.get_logged_in_user()}\nRam: {get_data.get_ram_usage()}%\nInternet: {get_data.is_connected_to_internet()},\nCPU Temp: {get_data.get_cpu_temperature()}"
        s.send(message.encode())


except Exception as e:
    print(f"Error: {e}")

finally:
    print("Closing connection")
    s.close()
