import time

import requests
import serial


def invia_stringa_seriale(dati_stringa) -> None:
    ser = serial.Serial(
        port="/dev/ttyUSB0",
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
    )

    if not ser.is_open:
        ser.open()

    # Converte stringa in bytes se necessario
    dati_bytes = dati_stringa.encode("utf-8")
    ser.write(dati_bytes)

    # Chiude la connessione
    ser.close()


if __name__ == "__main__":
    url_api = "http://localhost:5000/api/status"

    while True:
        risposta = requests.get(url_api)

        dati = risposta.json()
        stato = dati.get("status")
        if stato == "true":
            invia_stringa_seriale("T\n")
        elif stato == "false":
            invia_stringa_seriale("F\n")

        time.sleep(30)
