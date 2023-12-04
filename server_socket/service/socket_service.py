from client_socket.repository.client_socket_repository import ClientSocketRepository
from server_socket.repository.socket_repository import SocketRepository


class SocketService:
    def __init__(self):
        self.__socket_repository = SocketRepository()
        self.__client_socket_repository = ClientSocketRepository()

    def create_server_socket(self, host, port):
        return self.__socket_repository.create(host, port)

    def set_socket_option(self, api_control_level, option_name):
        self.__socket_repository.set_socket_option(api_control_level, option_name)

    def set_blocking_operation(self):
        self.__socket_repository.set_blocking_operation()

    def bind_server_socket(self):
        self.__socket_repository.bind_server_socket()

    def set_server_listen_number(self, count):
        self.__socket_repository.set_listen_number(count)

    def accept_client_socket(self):
        client_socket, client_address = self.__socket_repository.accept_client_socket()

        if client_socket is None:
            print("No client socket available.")
        else:
            print("client_socket: {}, client_address: {}".format(client_socket, client_address))
            self.__client_socket_repository.create_client_socket(client_socket, client_address)
            self.__client_socket_repository.set_blocking_operation()

    def get_client_socket_info(self):
        self.__client_socket_repository.get_client_socket()

    def close_server_socket(self):
        self.__socket_repository.close()
