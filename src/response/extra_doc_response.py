class ExtraDocResponse:
    __open_id: str
    __token: str
    __name: str
    __original_file: str
    __signed_file: str

    def __init__(self, open_id: str, token: str, name: str, original_file: str, signed_file: str):
        self.__open_id = open_id
        self.__token = token
        self.__name = name
        self.__original_file = original_file
        self.__signed_file = signed_file

    def get_open_id(self):
        return self.__open_id

    def set_open_id(self, open_id: str):
        self.__open_id = open_id

    def get_token(self):
        return self.__token

    def set_token(self, token: str):
        self.__token = token

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_original_file(self):
        return self.__original_file

    def set_original_file(self, original_file: str):
        self.__original_file = original_file

    def get_signed_file(self):
        return self.__signed_file

    def set_signed_file(self, signed_file: str):
        self.__signed_file = signed_file
