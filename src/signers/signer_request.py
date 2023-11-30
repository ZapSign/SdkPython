from src.services.json_converter import JsonConverter
from src.services.http_request_factory import HttpRequestFactory
from src.body.signer.signer import Signer
from src.body.signer.sign_batch import SignBatch

class SignerRequest:
    __api_route: str = 'https://api.zapsign.com.br/api/v1/'
    __json_converter: JsonConverter = JsonConverter()
    __api_token: str

    def __init__(self, api_token: str):
        self.__api_token = api_token

    def get_api_token(self):
        return self.__api_token

    def set_api_token(self, api_token: str):
        self.__api_token = api_token

    async def detail_signer(self, signer_token: str):
        url: str = f'{self.__api_route}signers/{signer_token}/?api_token={self.__api_token}'
        response = await HttpRequestFactory().get_request(url).response
        return self.__json_converter.json_to_signer(response)

    async def update_signer(self, signer_token: str, signer: Signer):
        # json_doc ?
        # Sugestão: json_signer
        json_doc: str = self.__json_converter.signer_to_json(signer)
        url: str = f'{self.__api_route}signers/{signer_token}/?api_token={self.__api_token}'
        response = await HttpRequestFactory().post_request(url, json_doc).response
        return self.__json_converter.json_to_signer(response)

    async def add_signer(self, doc_token: str, signer: Signer):
        json_doc: str = self.__json_converter.signer_to_json(signer)
        url: str = f'{self.__api_route}docs/{doc_token}/add-signer/?api_token={self.__api_token}'
        response = await HttpRequestFactory().post_request(url, json_doc).response
        return self.__json_converter.json_to_signer(response)

    # Em ts o parametro esta como doc_token !?!?!?
    async def delete_signer(self, signer_token: str):
        url: str = f'{self.__api_route}signer/{signer_token}/remove/?api_token={self.__api_token}'
        response = await HttpRequestFactory().delete_request(url).response
        return response

    async def sign_in_batch(self, sign_batch: SignBatch):
        # Sugestão mudar para json_sign_batch
        json_doc: str = self.__json_converter.sign_batch_to_json(sign_batch)
        url: str = f'{self.__api_route}sign/?api_token={self.__api_token}'
        response = await HttpRequestFactory().post_request(url, json_doc).response

        # Pode fazer isso ?
        return (await response).response