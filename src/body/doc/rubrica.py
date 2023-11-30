class Rubrica:
    __page: int = 0
    __relative_position_bottom: int = 0
    __relative_position_left: int = 0
    __relative_size_x: int = 0
    __relative_size_y: int = 0
    __type: str = ''
    __signer_token: str = ''

    def get_page(self):
        return self.__page

    def set_page(self, page: int):
        self.__page = page

    def get_relative_position_bottom(self):
        return self.__relative_position_bottom

    def set_relative_position_bottom(self, relative_position_bottom: int):
        self.__relative_position_bottom = relative_position_bottom

    def get_relative_position_left(self):
        return self.__relative_position_left

    def set_relative_position_left(self, relative_position_left: int):
        self.__relative_position_left = relative_position_left

    def get_relative_size_x(self):
        return self.__relative_size_x

    def set_relative_size_x(self, relative_size_x: int):
        self.__relative_size_x = relative_size_x

    def get_relative_size_y(self):
        return self.__relative_size_y

    def set_relative_size_y(self, relative_size_y: int):
        self.__relative_size_y = relative_size_y

    def get_type(self):
        return self.__type

    def set_type(self, type: str):
        self.__type = type

    def get_signer_token(self):
        return self.__signer_token

    def set_signer_token(self, signer_token: str):
        self.__signer_token = signer_token