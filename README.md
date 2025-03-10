# Raspberry Pi Bluetooth Server

This project implements a Bluetooth server on a Raspberry Pi that can receive string data from multiple Bluetooth hosts. The server is designed to handle incoming connections and process the received data efficiently.

## Project Structure

```
raspberry-pi-bluetooth-server
├── src
│   ├── server.py               # Main entry point for the Bluetooth server
│   ├── bluetooth_handler.py     # Handles Bluetooth connections and data processing
│   ├── config.py               # Configuration settings for the server
│   ├── utils
│   │   ├── __init__.py         # Empty initializer for the utils package
│   │   └── logging_utils.py     # Utility functions for logging events and errors
│   └── data
│       └── __init__.py         # Empty initializer for the data package
├── tests
│   ├── __init__.py             # Empty initializer for the tests package
│   └── test_bluetooth_handler.py # Unit tests for the BluetoothHandler class
├── logs                         # Directory for storing log files
├── requirements.txt             # Lists dependencies required for the project
├── setup.py                     # Setup script for the project
└── README.md                    # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd raspberry-pi-bluetooth-server
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the Bluetooth server, run the following command:

```
python src/server.py
```

The server will initialize the Bluetooth socket and begin listening for incoming connections. Once a connection is established, it will receive string data from the connected hosts.

## Logging

The server generates log files that can be found in the `logs` directory. These logs can help in tracking the server's operation and troubleshooting any issues that may arise.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.