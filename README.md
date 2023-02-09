# Python UDP Server

This is a basic implementation of a UDP server in Python, using the `socket` module. The server listens for incoming messages at the IP address `127.0.0.1` and port `25005`.

## Usage

The `send_message` function takes a `bytes` object as its only argument, representing the message to be sent. The function creates a new UDP socket, sets the target IP address and port, and sends the message.

If the script is run as the main module a sample message is created as a JSON-encoded `bytes` object and sent using the `send_message` function.

## Note

This code is just an example of a basic UDP server, and does not include error handling or robustness features that would be required in a production environment. The code is sourced from the [Python UDP Communication](https://wiki.python.org/moin/UdpCommunication) page on the Python wiki.
