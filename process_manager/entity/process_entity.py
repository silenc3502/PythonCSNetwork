class ProcessEntity:
    def __init__(self, process_id, target, args):
        self.__process_id = process_id
        self.__target = target
        self.__args = args

    def get_process_id(self):
        return self.__process_id

    def get_target(self):
        return self.__target

    def get_args(self):
        return self.__args