import bluetooth
import threading
from config import DIMENSIONE_BUFFER, TIMEOUT

# Variabili globali
connessioni = []
blocco_connessione = threading.Lock()
in_esecuzione = True


def thread_client(socket_client, info_client):
    """Funzione del thread per gestire la comunicazione con un client"""
    try:
        with blocco_connessione:
            connessioni.append(socket_client)

        print(f"client {info_client} connesso. Clienti totali: {len(connessioni)}")

        socket_client.settimeout(TIMEOUT)
        while in_esecuzione:
            try:
                dati = socket_client.recv(DIMENSIONE_BUFFER)
                if not dati:
                    break  # client disconnesso

                # Elabora i dati ricevuti
                messaggio = dati.decode("utf-8")
                elabora_dati(messaggio, info_client)

            except bluetooth.btcommon.BluetoothError as e:
                if "timed out" not in str(e):  # Ignora gli errori di timeout
                    print(f"Errore Bluetooth con il client {info_client}: {e}")
                    break
            except Exception as e:
                print(f"Errore con il client {info_client}: {e}")
                break

    finally:
        # Pulisci quando il client si disconnette
        with blocco_connessione:
            if socket_client in connessioni:
                connessioni.remove(socket_client)
        socket_client.close()
        print(f"client {info_client} disconnesso. Clienti rimanenti: {len(connessioni)}")


def gestisci_connessione(socket_client, info_client):
    """Avvia un nuovo thread per gestire una connessione client"""
    thread = threading.Thread(target=thread_client, args=(socket_client, info_client))
    thread.daemon = True
    thread.start()


def elabora_dati(dati, info_client):
    """Elabora i dati ricevuti da un client"""
    print(f"Dati da {info_client}: {dati}")
    # Aggiungi qui la tua logica di elaborazione dati
    # Per esempio, potresti salvare su un database, attivare
