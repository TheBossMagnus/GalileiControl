import os
import psutil
import socket
import requests

def get_logged_in_user():
    return os.getlogin()

def get_cpu_temperature():
    try:
        import wmi
        w = wmi.WMI(namespace="root\\wmi")
        temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
        temperature = temperature_info.CurrentTemperature
        return (temperature / 10.0) - 273.15 
    except ImportError:
        return "WMI module not installed"

def is_connected_to_internet():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

def get_ram_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

if __name__ == "__main__":
    user = get_logged_in_user()
    cpu_temp = get_cpu_temperature()
    internet_status = is_connected_to_internet()
    ram_usage = get_ram_usage()

    print(f"Logged in user: {user}")
    print(f"CPU Temperature: {cpu_temp} °C")
    print(f"Connected to Internet: {internet_status}")
    print(f"RAM Usage: {ram_usage}%")