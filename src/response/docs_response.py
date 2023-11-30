from typing import List
from src.response.doc_response import DocResponse
from src.response.extra_doc_response import ExtraDocResponse
from src.body.create_by import CreateBy
from src.body.template import Template
from src.body.answers import Answers


class DocsResponse:
    __count: int
    __next: str
    __previous: str
    __results: List[DocResponse]

    def __init__(self):
        self.__count = 0
        self.__next = ''
        self.__previous = ''
        self.__results = [
            DocResponse(0, '', '', '', '', '', [ExtraDocResponse('', '', '', '', '')], False, '', '', '', CreateBy(),
                        Template(''), [Answers('', '')], 0)]

    def get_count(self):
        return self.__count

    def set_count(self, count: int):
        self.__count = count

    def get_next(self):
        return self.__next

    def set_next(self, next: str):
        self.__next = next

    def get_previous(self):
        return self.__previous

    def set_previous(self, previous: str):
        self.__previous = previous

    def get_results(self):
        return self.__results

    def set_results(self, results: List[DocResponse]):
        self.__results = results
