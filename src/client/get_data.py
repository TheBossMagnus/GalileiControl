import os
import psutil
import requests


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
