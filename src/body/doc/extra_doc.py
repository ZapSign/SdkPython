class ExtraDoc:
    __name: str = ''
    __url_pdf: str = ''

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_url_pdf(self):
        return self.__url_pdf

    def set_url_pdf(self, url_pdf: str):
        self.__url_pdf = url_pdf