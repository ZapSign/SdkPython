from typing import List
from datetime import date
from src.body.signer.signer import Signer

class Doc:
    __sandbox: bool = False
    __name: str = ""
    __lang: str = "pt-br"
    __disable_signer_emails: bool = False
    __signed_file_only_finished: bool = False
    __brand_logo: str = ""
    __brand_primary_color: str = ""
    __brand_name: str = ""
    __external_id: str = ""
    __folder_path: str = "/"
    __date_limit_to_sign: date = date.today()
    __signature_order_active: bool = False
    __observers: List[str] = []
    __signers: List[Signer] = []
    __reminder_every_n_days: int = 0

    def get_sandbox(self):
        return self.__sandbox

    def set_sandbox(self, sandbox: bool):
        self.__sandbox = sandbox

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_lang(self):
        return self.__lang

    def set_lang(self, lang: str):
        self.__lang = lang

    def get_disable_signer_emails(self):
        return self.__disable_signer_emails

    def set_disable_signer_emails(self, disable_signer_emails: bool):
        self.__disable_signer_emails = disable_signer_emails

    def get_signed_file_only_finished(self):
        return self.__signed_file_only_finished

    def set_signed_file_only_finished(self, signed_file_only_finished: bool):
        self.__signed_file_only_finished = signed_file_only_finished

    def get_brand_logo(self):
        return self.__brand_logo

    def set_brand_logo(self, brand_logo: str):
        self.__brand_logo = brand_logo

    def get_brand_primary_color(self):
        return self.__brand_primary_color

    def set_brand_primary_color(self, brand_primary_color: str):
        self.__brand_primary_color = brand_primary_color

    def get_brand_name(self):
        return self.__brand_name

    def set_brand_name(self, brand_name: str):
        self.__brand_name = brand_name

    def get_external_id(self):
        return self.__external_id

    def set_external_id(self, external_id: str):
        self.__external_id = external_id

    def get_folder_path(self):
        return self.__folder_path

    def set_folder_path(self, folder_path: str):
        self.__folder_path = folder_path

    def get_date_limit_to_sign(self):
        return self.__date_limit_to_sign

    def set_date_limit_to_sign(self, date_limit_to_sign: date):
        self.__date_limit_to_sign = date_limit_to_sign

    def get_signature_order_active(self):
        return self.__signature_order_active

    def set_signature_order_active(self, signature_order_active: bool):
        self.__signature_order_active = signature_order_active

    def get_observers(self):
        return self.__observers

    def set_observers(self, observers: List[str]):
        self.__observers = observers

    def get_reminder_every_n_days(self):
        return self.__reminder_every_n_days

    def set_reminder_every_n_days(self, reminder_every_n_days: int):
        self.__reminder_every_n_days = reminder_every_n_days

    def get_signers(self):
        return self.__signers

    def set_signers(self, signers: List[Signer]):
        self.__signers = signers