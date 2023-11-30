from src.body.doc.doc import Doc

class DocFromDocx(Doc):
    __url_docx: str = ''

    def get_url_docx(self):
        return self.__url_docx

    def set_url_docx(self, url_docx: str):
        self.__url_docx = url_docx