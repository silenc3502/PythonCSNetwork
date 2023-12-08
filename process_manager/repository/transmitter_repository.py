from datetime import datetime as dt

import socket
import time

class TransmitterRepository:
    def __init__(self):
        print("TransmitterRepository Constructor")

    def transmit_command(self, client_socket, client_address):
        print("Is it operate ? (transmit_command)")

        while True:
            try:
                string_data = "test"
                client_socket.sendall(string_data.encode())
                print('{} command transmit [{}] from {}'.format(dt.now(), string_data, client_address[0]))

                time.sleep(0.5)

            except (socket.error, BrokenPipeError) as e:
                print(f"사용자 연결 종료!")
                return None

            except socket.error as e:
                print("Socket error:", e)
                time.sleep(0.5)

            # except queue.Empty:
                # print("socket_server_queue empty")
                # time.sleep(0.5)

            except Exception as ex:
                print("An error occurred:", ex)
