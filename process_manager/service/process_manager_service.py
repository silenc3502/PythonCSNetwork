from process_manager.repository.process_manager_repository import ProcessManagerRepository
from process_manager.repository.receiver_repository import ReceiverRepository
from process_manager.repository.transmitter_repository import TransmitterRepository


class ProcessManagerService:
    def __init__(self):
        self.__process_manager_repository = ProcessManagerRepository()
        self.__receiver_repository = ReceiverRepository()
        self.__transmitter_repository = TransmitterRepository()

    def create_process(self, target, args):
        return self.__process_manager_repository.create_process(target, args)

    def create_receiver_process(self, client_socket, client_address):
        return self.__process_manager_repository.create_process(
            target=self.__receiver_repository.receive_data,
            args=(client_socket, client_address,)
        )

    def create_transmitter_process(self, client_socket, client_address):
        return self.__process_manager_repository.create_process(
            target=self.__transmitter_repository.transmit_command,
            args=(client_socket, client_address,)
        )

    def get_processes(self):
        return self.__process_manager_repository.get_processes()

    def terminate_all_processes(self):
        self.__process_manager_repository.terminate_all_processes()
