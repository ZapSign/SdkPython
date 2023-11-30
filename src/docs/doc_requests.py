from src.services.json_converter import JsonConverter
from src.body.doc.doc_from_pdf import DocFromPdf
from src.services.http_request_factory import HttpRequestFactory
from src.body.doc.doc_from_docx import DocFromDocx
from src.body.doc.doc_from_template import DocFromTemplate
from src.body.doc.extra_doc import ExtraDoc
from src.body.doc.rubricas_array import RubricasArray

class DocRequests:
    __api_route: str = 'https://api.zapsign.com.br/api/v1/'
    __json_converter: JsonConverter = JsonConverter()
    __api_token: str = ''

    def __init__(self, api_token: str):
        self.__api_token = api_token

    # Por que duas funções iguais ? doc_requests/set_api_token
    def doc_requests(self, api_token: str):
        self.__api_token = api_token

    def get_api_token(self):
        return self.__api_token

    def set_api_token(self, api_token: str):
        self.__api_token = api_token

    async def create_doc_from_upload_pdf(self, doc: DocFromPdf):
        # Por que essa função é a unica que não cria nova instancia de JsonConverter ?
        json_doc: str = self.__json_converter.doc_from_pdf_to_json(doc)

        # Por que uri na sdk de ts ?
        url: str = f'{self.__api_route}docs/?api_token={self.__api_token}'

        # Como fazer destructuring assignment em python
        response = await HttpRequestFactory().post_request(url, json_doc).response
        return self.__json_converter.json_to_docs_response(response)

    async def get_docs(self):
        url: str = f'{self.__api_route}docs/?api_token={self.__api_token}'
        response = await HttpRequestFactory().get_request(url).response
        return self.__json_converter.json_to_docs_response(response)

    async def create_doc_from_upload_docx(self, doc: DocFromDocx):
        json_doc: str = JsonConverter().doc_from_docx_to_json(doc)
        url: str = f'{self.__api_route}docs/?api_token={self.__api_token}'
        response = await HttpRequestFactory().post_request(url, json_doc).response
        # Por que para pdf se usa json_to_docS_response e docx json_to_doc_response ?
        return self.__json_converter.json_to_doc_response(response)

    async def create_doc_from_upload_async(self, doc: DocFromPdf):
        json_doc: str = JsonConverter().doc_from_pdf_to_json(doc)
        url: str = f'{self.__api_token}docs/async/?api_token={self.__api_token}'
        response = await HttpRequestFactory().post_request(url, json_doc).response
        return self.__json_converter.json_to_doc_async_response(response)

    async def create_from_template(self, doc: DocFromTemplate):
        json_doc: str = JsonConverter().doc_from_template_to_json(doc)
        url: str =  f'{self.__api_route}models/create-doc/?api_token={self.__api_token}'
        response = await HttpRequestFactory().post_request(url, json_doc).response
        return self.__json_converter.json_to_doc_response(response)

    async def create_from_template_async(self, doc: DocFromTemplate):
        json_doc: str = JsonConverter.doc_from_template_to_json(doc)
        url: str = f'{self.__api_route}models/create-doc/async/?api_token={self.__api_token}'
        response = await HttpRequestFactory().post_request(url, json_doc).response
        return self.__json_converter.json_to_doc_async_response(response)

    async def add_extra_doc(self, doc_token: str, extra_doc: ExtraDoc):
        json_doc: str = JsonConverter().extra_docs_to_json(extra_doc)
        url: str = f'{self.__api_route}docs/{doc_token}/upload-extra-doc/?api_token={self.__api_token}'
        response = await HttpRequestFactory().post_request(url, json_doc).response
        return self.__json_converter.json_to_extra_doc_response(response)

    async def detail_doc(self, doc_token: str):
        url: str = f'{self.__api_route}docs/{doc_token}/?api_token={self.__api_token}'
        response = await HttpRequestFactory().get_request(url).response
        return self.__json_converter.json_to_doc_response(response)

    async def delete_doc(self, doc_token: str):
        url: str = f'{self.__api_route}docs/{doc_token}/?api_token={self.__api_token}'
        response = await HttpRequestFactory().delete_request(url).response
        return self.__json_converter.json_to_doc_response(response)

    # Padronizar nome de rubricas se vai ser utilizado array ou list
    async def place_signatures(self, doc_token: str, rubrica_list: RubricasArray):
        json_doc: str = JsonConverter().rubricas_array_to_json(rubrica_list)
        url: str = f'{self.__api_route}docs/{doc_token}/place-signatures/?api_token={self.__api_token}'
        response = await HttpRequestFactory().post_request(url, json_doc).response
        return response