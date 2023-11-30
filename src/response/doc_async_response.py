class DocAsyncResponse:
    __token: str

    def __init__(self, token: str):
        self.__token = token

    def get_token(self):
        return self.__token

    def set_token(self, token: str):
        self.__token = token