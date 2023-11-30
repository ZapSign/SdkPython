from src.body.doc.rubrica import Rubrica
from typing import List

class RubricasArray:
    __rubricas: List[Rubrica]

    def __init__(self, rubricas: List[Rubrica]):
        self.__rubricas = rubricas

    def get_rubricas(self):
        return self.__rubricas

    def set_rubricas(self, rubricas: List[Rubrica]):
        self.__rubricas = rubricas