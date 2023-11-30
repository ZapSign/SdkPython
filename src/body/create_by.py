class CreateBy:
    __email: str = ''

    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        self.__email = email