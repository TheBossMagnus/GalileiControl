import bluetooth
import signal
import sys
import threading
from config import BLUETOOTH_DEVICE_NAME, BLUETOOTH_UUID, MAX_CONNECTIONS
import bluetooth_handler

# Global variable for server socket
server_socket = None

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\nShutting down server...")
    bluetooth_handler.close_all()
    if server_socket:
        server_socket.close()
    sys.exit(0)

def initialize_server():
    """Initialize the Bluetooth server socket"""
    global server_socket
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(("", bluetooth.PORT_ANY))
    server_socket.listen(MAX_CONNECTIONS)
    
    port = server_socket.getsockname()[1]
    
    # Advertise the service
    bluetooth.advertise_service(
        server_socket, 
        BLUETOOTH_DEVICE_NAME,
        service_id=BLUETOOTH_UUID,
        service_classes=[BLUETOOTH_UUID, bluetooth.SERIAL_PORT_CLASS],
        profiles=[bluetooth.SERIAL_PORT_PROFILE]
    )
    
    print(f"Started Bluetooth server '{BLUETOOTH_DEVICE_NAME}'")
    print(f"Listening for connections on RFCOMM channel {port}")
    print("Press Ctrl+C to stop the server")
    
    return server_socket

def main():
    global server_socket
    
    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Initialize the server
    server_socket = initialize_server()
    
    try:
        while True:
            # Accept connections in the main thread
            client_socket, client_info = server_socket.accept()
            # Pass the connection to the handler
            bluetooth_handler.handle_connection(client_socket, client_info)
            
    except KeyboardInterrupt:
        print("\nServer interrupted by user")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        print("Cleaning up resources...")
        bluetooth_handler.close_all()
        server_socket.close()
        print("Server stopped")

if __name__ == "__main__":
    main()