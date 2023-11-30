from src.body.signer.signer import Signer

class SignerBuilder:
    signer: Signer

    def __init__(self):
        self.signer = Signer()

    def with_name(self, name: str):
        self.signer.set_name(name)
        return self

    def with_email(self, email: str):
        self.signer.set_email(email)
        return self

    def with_auth_mode(self, auth_mode: str):
        self.signer.set_auth_mode(auth_mode)
        return self

    def with_send_automatic_email(self, send_automatic_email: bool):
        self.signer.set_send_automatic_email(send_automatic_email)
        return self

    def with_send_automatic_whatsapp(self, send_automatic_whatsapp: bool):
        self.signer.set_send_automatic_whatsapp(send_automatic_whatsapp)
        return self

    def with_order_group(self, order_group: int):
        self.signer.set_order_group(order_group)
        return self

    def with_custom_message(self, custom_message: str):
        self.signer.set_custom_message(custom_message)
        return self

    def with_phone_country(self, phone_country: str):
        self.signer.set_phone_country(phone_country)
        return self

    def with_phone_number(self, phone_number: str):
        self.signer.set_phone_number(phone_number)
        return self

    def with_lock_email(self, lock_email: bool):
        self.signer.set_lock_email(lock_email)
        return self

    def with_blank_email(self, blank_email: bool):
        self.signer.set_blank_email(blank_email)
        return self

    def with_hide_email(self, hide_email: bool):
        self.signer.set_hide_email(hide_email)
        return self

    def with_lock_phone(self, lock_phone: bool):
        self.signer.set_lock_phone(lock_phone)
        return self

    def with_blank_phone(self, blank_phone: bool):
        self.signer.set_blank_phone(blank_phone)
        return self

    def with_hide_phone(self, hide_phone: bool):
        self.signer.set_hide_phone(hide_phone)
        return self

    def with_lock_name(self, lock_name: bool):
        self.signer.set_lock_name(lock_name)
        return self

    def with_require_selfie_photo(self, require_selfie_photo: bool):
        self.signer.set_require_selfie_photo(require_selfie_photo)
        return self

    def with_qualification(self, qualification: str):
        self.signer.set_qualification(qualification)
        return self

    def with_external_id(self, external_id: str):
        self.signer.set_external_id(external_id)
        return self

    def with_redirect_link(self, redirect_link: str):
        self.signer.set_redirect_link(redirect_link)
        return self

    def with_sign_url(self, sign_url: str):
        self.signer.set_sign_url(sign_url)
        return self

    def with_token(self, token: str):
        self.signer.set_token(token)
        return self

    def with_status(self, status: str):
        self.signer.set_status(status)
        return self

    def with_last_view_at(self, last_view_at: str):
        self.signer.set_last_view_at(last_view_at)
        return self

    def with_signed_at(self, signed_at: str):
        self.signer.set_signed_at(signed_at)
        return self

    def with_geo_latitude(self, geo_latitude: str):
        self.signer.set_geo_latitude(geo_latitude)
        return self

    def with_geo_longitude(self, geo_longitude: str):
        self.signer.set_geo_longitude(geo_longitude)
        return self

    def with_signature_image(self, signature_image: str):
        self.signer.set_signature_image(signature_image)
        return self

    def with_visto_image(self, visto_image: str):
        self.signer.set_visto_image(visto_image)
        return self

    def with_document_photo_url(self, document_photo_url: str):
        self.signer.set_document_photo_url(document_photo_url)
        return self

    def with_document_verse_photo_url(self, document_verse_photo_url: str):
        self.signer.set_document_verse_photo_url(document_verse_photo_url)
        return self

    def with_selfie_photo_url2(self, selfie_photo_url2: str):
        self.signer.set_selfie_photo_url2(selfie_photo_url2)
        return self

    def with_send_via(self, send_via: str):
        self.signer.set_send_via(send_via)
        return self

    def with_require_document_photo(self, require_document_photo: str):
        self.signer.set_require_document_photo(require_document_photo)
        return self

    def build(self):
        return self.signer