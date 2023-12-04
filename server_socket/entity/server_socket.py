import atexit


class ServerSocket:
    def __init__(self, host, port, socket):
        self.__host = host
        self.__port = port
        self.__socket = socket

        atexit.register(self.close_socket)

    def get_host(self):
        return self.__host

    def get_port(self):
        return self.__port

    def get_socket(self):
        return self.__socket

    def close_socket(self):
        print("Close Socket")
        self.__socket.close()

