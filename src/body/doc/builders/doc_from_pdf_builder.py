from src.body.doc.doc_from_pdf import DocFromPdf
from src.body.signer.signer import Signer
from datetime import date
from typing import List

class DocFromPdfBuilder:
    doc_from_pdf: DocFromPdf

    def __init__(self):
        self.doc_from_pdf = DocFromPdf()

    def with_sandbox(self, sandbox: bool):
        self.doc_from_pdf.set_sandbox(sandbox)
        return self

    def with_name(self, name: str):
        self.doc_from_pdf.set_name(name)
        return self

    def with_lang(self, lang: str):
        self.doc_from_pdf.set_lang(lang)
        return self

    def with_disable_signer_emails(self, disable_signer_emails: bool):
        self.doc_from_pdf.set_disable_signer_emails(disable_signer_emails)
        return self

    def with_signed_file_only_finished(self, signed_file_only_finished: bool):
        self.doc_from_pdf.set_signed_file_only_finished(signed_file_only_finished)
        return self

    def with_brand_logo(self, brand_logo: str):
        self.doc_from_pdf.set_brand_logo(brand_logo)
        return self

    def with_brand_primary_color(self, brand_primary_color: str):
        self.doc_from_pdf.set_brand_primary_color(brand_primary_color)
        return self

    def with_brand_name(self, brand_name: str):
        self.doc_from_pdf.set_brand_name(brand_name)
        return self

    def with_external_id(self, external_id: str):
        self.doc_from_pdf.set_external_id(external_id)
        return self

    def with_folder_path(self, folder_path: str):
        self.doc_from_pdf.set_folder_path(folder_path)
        return self

    def with_date_limit_to_sign(self, date_limit_to_sign: date):
        self.doc_from_pdf.set_date_limit_to_sign(date_limit_to_sign)
        return self

    def with_signature_order_active(self, signature_order_active: bool):
        self.doc_from_pdf.set_signature_order_active(signature_order_active)
        return self

    def with_observers(self, observers: List[str]):
        self.doc_from_pdf.set_observers(observers)
        return self

    def with_reminder_every_n_days(self, reminder_every_n_days: int):
        self.doc_from_pdf.set_reminder_every_n_days(reminder_every_n_days)
        return self

    def with_signers(self, signers: List[Signer]):
        self.doc_from_pdf.set_signers(signers)
        return self

    def with_url_pdf(self, url_pdf):
        self.doc_from_pdf.set_url_pdf(url_pdf)
        return self

    def build(self):
        return self.doc_from_pdf