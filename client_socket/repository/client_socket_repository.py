from client_socket.entity.client_socket import ClientSocket


class ClientSocketRepository:
    def __init__(self):
        self.__client_socket = None

    def create_client_socket(self, client_socket, client_address):
        self.__client_socket = ClientSocket(client_socket, client_address)

    def set_blocking_operation(self):
        client_socket = self.__client_socket.get_socket()
        client_socket.setblocking(False)

    def get_client_socket(self):
        client_socket = self.__client_socket.get_socket()
        client_address = self.__client_socket.get_address()
        return client_socket, client_address
