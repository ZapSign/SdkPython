from src.body.doc.doc import Doc
from src.body.doc.de_para_template import DeParaTemplate
from typing import List

class DocFromTemplate(Doc):
    __signer_name: str = ''
    __template_id: str = ''
    __data: List[DeParaTemplate] = [DeParaTemplate()]


    def get_signer(self):
        raise Exception('You can not set signers in DocFromTemplate, try setSigner_name.')

    def set_signer(self):
        raise Exception('You can not set signers in DocFromTemplate, try setSigner_name.')

    def get_signer_name(self):
        return self.__signer_name

    def set_signer_name(self, signer_name: str):
        self.__signer_name = signer_name

    def get_template_id(self):
        return self.__template_id

    def set_template_id(self, template_id: str):
        self.__template_id = template_id

    def get_data(self):
        return self.__data

    def set_data(self, data: List[DeParaTemplate]):
        self.__data = data