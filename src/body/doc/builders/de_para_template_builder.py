from src.body.doc.de_para_template import DeParaTemplate

class DeParaTemplateBuilder:
    de_para_template: DeParaTemplate

    def __init__(self):
        self.de_para_template = DeParaTemplate()

    def de(self, de: str):
        self.de_para_template.set_de(de)
        return self

    def para(self, para: str):
        self.de_para_template.set_para(para)
        return self

    def build(self):
        return self.de_para_template