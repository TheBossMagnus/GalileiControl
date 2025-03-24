import os
import psutil
import requests
import socket


def organizza_dati():
    data = {"hostname": get_hostname(),
            "username": get_logged_in_user(), 
            "info": {"cpu_temperature": get_cpu_temperature(), "internet_connection": is_connected_to_internet(), "ram_usage": get_ram_usage()}}
    return data

def get_hostname():
    return socket.gethostname()


def get_logged_in_user():
    return os.getlogin()


def get_cpu_temperature():
    return "TBD"


def is_connected_to_internet():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


def get_ram_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent
