import socket
import time

from datetime import datetime as dt
from process_manager.entity.receiver_message import ReceiverMessage


class ReceiverRepository:
    def __init__(self):
        print("ReceiverRepository Constructor")

    def receive_data(self, client_socket, client_address):
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Client disconnected!")
                client_socket.close()
                return None

            response_data = data.decode().strip()
            print('{} command received [{}] from {}'.format(dt.now(), response_data, client_address[0]))

            time.sleep(0.5)
            return ReceiverMessage(response_data, client_address)

        except socket.error:
            time.sleep(0.5)
            return None