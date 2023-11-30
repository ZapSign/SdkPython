class Answers:
    __variable: str
    __value: str

    def __init__(self, variable: str, value: str):
        self.__variable = variable
        self.__value = value

    def get_variable(self):
        return self.__variable

    def set_variable(self, variable: str):
        self.__variable = variable

    def get_value(self):
        return self.__value

    def set_value(self, value: str):
        self.__value = value
