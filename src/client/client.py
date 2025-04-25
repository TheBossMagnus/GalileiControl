import socket
import time

from get_data import organizza_dati

indirizzo_server = "2C:CF:67:99:D4:0E"
porta = 3

socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    print(f"Connessione al server {indirizzo_server}...")
    socket.connect((indirizzo_server, porta))
    print("Connessione avvenuta con successo")

    while True:
        time.sleep(5)
        dati_da_inviare = organizza_dati()
        socket.send(dati_da_inviare.encode())

except Exception as e:
    print(f"Errore: {e}")

finally:
    print("Chiusura connessione")
    socket.close()
