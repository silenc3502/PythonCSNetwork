import multiprocessing as mp
from process_manager.entity.process_entity import ProcessEntity


class ProcessManagerRepository:
    def __init__(self):
        self.__processes = []

    def create_process(self, target, args):
        new_process = mp.Process(target=target, args=args)
        new_process.start()
        process_entity = ProcessEntity(new_process.pid, target, args)
        self.__processes.append(process_entity)
        return process_entity

    def get_processes(self):
        return self.__processes

    def terminate_all_processes(self):
        for process_entity in self.__processes:
            process = mp.Process(target=process_entity.get_target(), args=process_entity.get_args())
            process.terminate()
