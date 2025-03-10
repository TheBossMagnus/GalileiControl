import bluetooth
import threading
from config import BUFFER_SIZE, TIMEOUT

# Global variables
connections = []
connection_lock = threading.Lock()
running = True

def client_thread(client_socket, client_info):
    """Thread function to handle communication with a client"""
    try:
        with connection_lock:
            connections.append(client_socket)
        
        print(f"Client {client_info} connected. Total clients: {len(connections)}")
        
        client_socket.settimeout(TIMEOUT)
        while running:
            try:
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break  # Client disconnected
                
                # Process received data
                message = data.decode('utf-8')
                process_data(message, client_info)
                
            except bluetooth.btcommon.BluetoothError as e:
                if "timed out" not in str(e):  # Ignore timeout errors
                    print(f"Bluetooth error with client {client_info}: {e}")
                    break
            except Exception as e:
                print(f"Error with client {client_info}: {e}")
                break
    
    finally:
        # Clean up when client disconnects
        with connection_lock:
            if client_socket in connections:
                connections.remove(client_socket)
        client_socket.close()
        print(f"Client {client_info} disconnected. Remaining clients: {len(connections)}")

def handle_connection(client_socket, client_info):
    """Start a new thread to handle a client connection"""
    thread = threading.Thread(target=client_thread, args=(client_socket, client_info))
    thread.daemon = True
    thread.start()

def process_data(data, client_info):
    """Process data received from a client"""
    print(f"Data from {client_info}: {data}")
    # Add your data processing logic here
    # For example, you could save to a database, trigger