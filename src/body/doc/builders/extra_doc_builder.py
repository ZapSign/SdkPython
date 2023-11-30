from src.body.doc.extra_doc import ExtraDoc

class ExtraDocBuilder:
    extra_doc: ExtraDoc

    def __init__(self):
        self.extra_doc = ExtraDoc()

    def with_name(self, name: str):
        self.extra_doc.set_name(name)
        return self

    def with_url_pdf(self, url_pdf: str):
        self.extra_doc.set_url_pdf(url_pdf)
        return self

    def build(self):
        return self.extra_doc