import json
import os
import socket
from typing import Optional

import psutil
import requests
import WinTmp


def organizza_dati():
    # Restituisce tutti i dati direttamente senza nidificarli sotto 'info'
    dati = {
        "nome_utente": get_utente_connesso(),
        "temperatura_cpu": get_temperatura_cpu(),
        "connessione_internet": è_connesso_a_internet(),
        "uso_ram": get_uso_ram(),
    }
    return json.dumps({"nome_host": get_nome_host(), "dati": dati})


def get_nome_host():
    return socket.gethostname()


def get_utente_connesso():
    return os.getlogin()


def get_temperatura_cpu():
    return WinTmp.CPU_Temp()


def è_connesso_a_internet() -> Optional[bool]:
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


def get_uso_ram():
    informazioni_memoria = psutil.virtual_memory()
    return informazioni_memoria.percent
