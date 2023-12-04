import atexit


class ClientSocket:
    def __init__(self, socket):
        self.__socket = socket

        # atexit.register(self.close_socket)

    def get_socket(self):
        return self.__socket
