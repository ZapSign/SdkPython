from src.body.doc.doc import Doc

class DocFromPdf(Doc):
    __url_pdf: str or None = None

    def get_url_pdf(self):
        return self.__url_pdf

    def set_url_pdf(self, url_pdf: str):
        self.__url_pdf = url_pdf