import bluetooth
import signal
import sys
import threading
from config import BLUETOOTH_DEVICE_NAME, BLUETOOTH_UUID, MAX_CONNECTIONS
import bluetooth_handler

# Variabile globale per il socket del server
socket_server = None

def inizializza_server():
    """Inizializza il socket del server Bluetooth"""
    global socket_server
    socket_server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket_server.bind(("", 3))
    socket_server.listen(MAX_CONNECTIONS)
    
    porta = socket_server.getsockname()[1]
    
    # Pubblicizza il servizio
    bluetooth.advertise_service(
        socket_server, 
        BLUETOOTH_DEVICE_NAME,
        service_id=BLUETOOTH_UUID,
        service_classes=[BLUETOOTH_UUID, bluetooth.SERIAL_PORT_CLASS],
        profiles=[bluetooth.SERIAL_PORT_PROFILE]
    )
    
    print(f"Server Bluetooth '{BLUETOOTH_DEVICE_NAME}' avviato")
    print(f"In ascolto per connessioni sul canale RFCOMM {porta}")
    print("Premi Ctrl+C per fermare il server")
    
    return socket_server

def main():
    global socket_server
    # Inizializza il server
    socket_server = inizializza_server()
    
    try:
        while True:
            # Accetta connessioni nel thread principale
            socket_client, info_client = socket_server.accept()
            # Passa la connessione al gestore
            bluetooth_handler.handle_connection(socket_client, info_client)
            
    except KeyboardInterrupt:
        print("\nServer interrotto dall'utente")
    except Exception as e:
        print(f"Errore del server: {e}")
    finally:
        print("Pulizia delle risorse in corso...")
        bluetooth_handler.close_all()
        socket_server.close()
        print("Server fermato")

if __name__ == "__main__":
    main()