import json
from src.response.doc_response import DocResponse
from src.response.docs_response import DocsResponse
from src.response.doc_async_response import DocAsyncResponse
from src.response.extra_doc_response import ExtraDocResponse
from src.body.doc.doc_from_pdf import DocFromPdf
from src.body.doc.doc_from_docx import DocFromDocx
from src.body.doc.doc_from_template import DocFromTemplate
from src.body.doc.extra_doc import ExtraDoc
from src.body.doc.rubricas_array import RubricasArray
from src.body.signer.signer import Signer
from src.body.signer.sign_batch import SignBatch

class JsonConverter:

    def doc_response_to_json(self, doc_response: DocResponse):
        return json.dumps(doc_response)

    def docs_response_to_json(self, docs_response: DocsResponse):
        return json.dumps(docs_response)

    def doc_async_response_to_json(self, doc_async_response: DocAsyncResponse):
        return json.dumps(doc_async_response)

    def extra_doc_to_json(self, extra_doc_response: ExtraDocResponse):
        return json.dumps(extra_doc_response)

    def doc_from_pdf_to_json(self, doc_from_pdf: DocFromPdf):
        return json.dumps(doc_from_pdf)

    def doc_from_docx_to_json(self, doc_from_docx: DocFromDocx):
        return json.dumps(doc_from_docx)

    def doc_from_template_to_json(self, doc_from_template: DocFromTemplate):
        return json.dumps(doc_from_template)

    def extra_docs_to_json(self, extra_docs: ExtraDoc):
        return json.dumps(extra_docs)

    def rubricas_array_to_json(self, rubricas_array: RubricasArray):
        return json.dumps(rubricas_array)

    def signer_to_json(self, signer: Signer):
        return json.dumps(signer)

    def sign_batch_to_json(self, sign_batch: SignBatch):
        return json.dumps(sign_batch)

    # Iguais ?? json_to_doc_response e json_to_docs_response
    def json_to_doc_response(self, json_response: str):
        return json.loads(json.dumps(json_response))

    def json_to_docs_response(self, json_response: str):
        return json.loads(json.dumps(json_response))

    def json_to_doc_async_response(self, json_response: str):
        return json.loads(json.dumps(json_response))

    def json_to_extra_doc_response(self, json_response: str):
        return json.loads(json.dumps(json_response))

    def json_to_signer(self, json_response: str):
        return json.loads(json.dumps(json_response))
