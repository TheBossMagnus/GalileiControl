import serial
import time
import requests 
import json 

def send_serial_string(string_data):
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    
    if not ser.is_open:
        ser.open()
        

    # Convert string to bytes if needed
    data_bytes = string_data.encode('utf-8')
    ser.write(data_bytes)
    
    # Close the connection
    ser.close()
        

if __name__ == "__main__":
    api_url = "http://localhost:5000/api/status"

    while True:
        response = requests.get(api_url)
        
        data = response.json()
        status = data.get("status")
        if status == "true":
            send_serial_string("T\n")
        elif status == "false":
            send_serial_string("F\n")


        time.sleep(30)

