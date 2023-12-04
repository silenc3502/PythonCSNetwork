import socket
from time import sleep

from process_manager.service.process_manager_service import ProcessManagerService
from server_socket.service.socket_service import SocketService

socket_service = SocketService()
socket_service.create_server_socket("localhost", 33333)
socket_service.set_socket_option(socket.SOL_SOCKET, socket.SO_REUSEADDR)
socket_service.bind_server_socket()
socket_service.set_server_listen_number(1)
socket_service.set_blocking_operation()

process_manager_service = ProcessManagerService()

while True:
    try:
        socket_service.accept_client_socket()

        client, address = socket_service.get_client_socket_info()
        process_manager_service.create_receiver_process(client, address)

    except socket.error:
        sleep(0.5)
