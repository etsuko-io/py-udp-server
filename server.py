"""
Python UDP server. Source: https://wiki.python.org/moin/UdpCommunication
"""
import json
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 25005


def send_message(message: bytes):
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    sock = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_DGRAM,  # UDP
    )
    sock.sendto(message, (UDP_IP, UDP_PORT))


if __name__ == "__main__":
    _message = json.dumps({
        "service": "worker_server",
        "processing_time": 0.04387,
    }).encode()
    print(f"message: {_message}")
    send_message(_message)
