import socket
from python_socket.entity.python_socket import PythonSocket


class SocketRepository:
    def __init__(self):
        self.__python_server_socket = None

    def create(self, host, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__python_server_socket = PythonSocket(host, port, server_socket)

        return self.__python_server_socket

    def set_socket_option(self, api_control_level, option_name):
        server_socket = self.__python_server_socket.get_socket()
        server_socket.setsockopt(api_control_level, option_name, 1)

    def set_blocking_operation(self):
        server_socket = self.__python_server_socket.get_socket()
        server_socket.setblocking(False)

    def bind_server_socket(self):
        server_socket = self.__python_server_socket.get_socket()
        server_socket.bind((
            self.__python_server_socket.get_host(),
            self.__python_server_socket.get_port(),
        ))

    def close(self):
        server_socket = self.__python_server_socket.get_socket()
        server_socket.close()

        self.__python_server_socket = None



