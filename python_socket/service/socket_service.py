from python_socket.repository.socket_repository import SocketRepository


class SocketService:
    def __init__(self):
        self.__socket_repository = SocketRepository()

    def create_server_socket(self, host, port):
        return self.__socket_repository.create(host, port)

    def set_socket_option(self, api_control_level, option_name):
        self.__socket_repository.set_socket_option(api_control_level, option_name)

    def set_blocking_operation(self):
        self.__socket_repository.set_blocking_operation()

    def bind_server_socket(self):
        self.__socket_repository.bind_server_socket()

    def close_server_socket(self):
        self.__socket_repository.close()
