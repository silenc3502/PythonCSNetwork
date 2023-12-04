import atexit


class ClientSocket:
    def __init__(self, socket, address):
        self.__socket = socket
        self.__address = address

        # atexit.register(self.close_socket)

    def get_socket(self):
        return self.__socket

    def get_address(self):
        return self.__address
