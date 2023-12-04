import socket

from python_socket.service.socket_service import SocketService

socket_service = SocketService()
socket_service.create_server_socket("localhost", 33333)
socket_service.set_socket_option(socket.SOL_SOCKET, socket.SO_REUSEADDR)
socket_service.bind_server_socket()

