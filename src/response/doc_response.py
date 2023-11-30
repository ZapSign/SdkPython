from src.body.doc.doc import Doc
from src.response.extra_doc_response import ExtraDocResponse
from src.body.create_by import CreateBy
from src.body.template import Template
from src.body.answers import Answers
from typing import List


class DocResponse(Doc):
    __open_id: int = 0
    __token: str = ''
    __status: str = ''
    __original_file: str = ''
    __signed_file: str = ''
    __created_through: str = ''
    __extra_docs: List[ExtraDocResponse] = [ExtraDocResponse('', '', '', '', '')]
    __deleted: bool = False
    __deleted_at: str = ''
    __created_at: str = ''
    __last_update_at: str = ''
    __created_by: CreateBy = CreateBy()
    __template: Template = Template('')
    __answers: List[Answers] = [Answers('', '')]
    __auto_reminder: int = 0

    def __init__(self, open_id: int,
                 token: str,
                 status: str,
                 original_file: str,
                 signed_file: str,
                 created_through: str,
                 extra_docs: List[ExtraDocResponse],
                 deleted: bool,
                 deleted_at: str,
                 created_at: str,
                 last_update_at: str,
                 created_by: CreateBy,
                 template: Template,
                 answers: List[Answers],
                 auto_reminder: int):
        super().__init__()
        self.__open_id = open_id
        self.__token = token
        self.__status = status
        self.__original_file = original_file
        self.__signed_file = signed_file
        self.__created_through = created_through
        self.__extra_docs = extra_docs
        self.__deleted = deleted
        self.__deleted_at = deleted_at
        self.__created_at = created_at
        self.__last_update_at = last_update_at
        self.__created_by = created_by
        self.__template = template
        self.__answers = answers
        self.__auto_reminder = auto_reminder

    def get_open_id(self):
        return self.__open_id

    def set_open_id(self, open_id: int):
        self.__open_id = open_id

    def get_token(self):
        return self.__token

    def set_token(self, token: str):
        self.__token = token

    def get_status(self):
        return self.__status

    def set_status(self, status: str):
        self.__status = status

    def get_original_file(self):
        return self.__original_file

    def set_original_file(self, original_file: str):
        self.__original_file = original_file

    def get_signed_file(self):
        return self.__signed_file

    def set_signed_file(self, signed_file: str):
        self.__signed_file = signed_file

    def get_created_through(self):
        return self.__created_through

    def set_created_through(self, created_through: str):
        self.__created_through = created_through

    def get_extra_docs(self):
        return self.__extra_docs

    def set_extra_docs(self, extra_docs: List[ExtraDocResponse]):
        self.__extra_docs = extra_docs

    def get_deleted(self):
        return self.__deleted

    def set_deleted(self, deleted: bool):
        self.__deleted = deleted

    def get_deleted_at(self):
        return self.__deleted_at

    def set_deleted_at(self, deleted_at: str):
        self.__deleted_at = deleted_at

    def get_created_at(self):
        return self.__created_at

    def set_created_at(self, created_at: str):
        self.__created_at = created_at

    def get_last_update_at(self):
        return self.__last_update_at

    def set_last_update_at(self, last_update_at: str):
        self.__last_update_at = last_update_at

    def get_created_by(self):
        return self.__created_by

    def set_created_by(self, created_by: CreateBy):
        self.__created_by = created_by

    def get_template(self):
        return self.__template

    def set_template(self, template: Template):
        self.__template = template

    def get_answers(self):
        return self.__answers

    def set_answers(self, answers: List[Answers]):
        self.__answers = answers

    def get_auto_reminder(self):
        return self.__auto_reminder

    def set_auto_reminder(self, auto_reminder: int):
        self.__auto_reminder = auto_reminder
