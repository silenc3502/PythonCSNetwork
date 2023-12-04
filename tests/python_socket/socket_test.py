import unittest

from python_socket.entity.python_socket import PythonSocket
from python_socket.service.socket_service import SocketService


class TestPythonSocket(unittest.TestCase):
    def setUp(self):
        self.socket_service = SocketService()
        self.host = "localhost"
        self.port = 8080
        self.socket_instance = self.socket_service.create_server_socket(self.host, self.port)

    def test_get_host(self):
        self.assertEqual(self.socket_instance.get_host(), self.host)

    def test_get_port(self):
        self.assertEqual(self.socket_instance.get_port(), self.port)

if __name__ == '__main__':
    unittest.main()
