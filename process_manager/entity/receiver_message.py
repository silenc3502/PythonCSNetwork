class ReceiverMessage:
    def __init__(self):
        self.__data = None

    def set_receiver_message_data(self, data):
        self.__data = data

    def get_receiver_message_data(self):
        return self.__data


