class Signer:
    __name: str = ''
    __email: str = ''
    __auth_mode: str = 'assinaturaTela'
    __send_automatic_email: bool = False
    __send_automatic_whatsapp: bool = False
    __order_group: int = 0
    __custom_message: str = ''
    __phone_country: str = ''
    __phone_number: str = ''
    __lock_email: bool = False
    __blank_email: bool = False
    __hide_email: bool = False
    __lock_phone: bool = False
    __blank_phone: bool = False
    __hide_phone: bool = False
    __lock_name: bool = False
    __require_selfie_photo: bool = False
    __selfie_validation_type: str = "none"
    __qualification: str = ''
    __external_id: str = ''
    __redirect_link: str = ''
    __sign_url: str = ''
    __token: str = ''
    __status: str = ''
    __times_viewed: int = 0
    __last_view_at: str = ''
    __signed_at: str = ''
    __geo_latitude: str = ''
    __geo_longitude: str = ''
    __signature_image: str = ''
    __visto_image: str = ''
    __document_photo_url: str = ''
    __document_verse_photo_url: str = ''
    __selfie_photo_url: str = ''
    __selfie_photo_url2: str = ''
    __send_via: str = ''
    __require_document_photo: str = ''

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def get_auth_mode(self):
        return self.__auth_mode

    def set_auth_mode(self, auth_mode: str):
        self.__auth_mode = auth_mode

    def get_send_automatic_email(self):
        return self.__send_automatic_email

    def set_send_automatic_email(self, send_automatic_email: bool):
        self.__send_automatic_email = send_automatic_email

    def get_send_automatic_whatsapp(self):
        return self.__send_automatic_whatsapp

    def set_send_automatic_whatsapp(self, send_automatic_whatsapp: bool):
        self.__send_automatic_whatsapp = send_automatic_whatsapp

    def get_order_group(self):
        return self.__order_group

    def set_order_group(self, order_group: int):
        self.__order_group = order_group

    def get_custom_message(self):
        return self.__custom_message

    def set_custom_message(self, custom_message: str):
        self.__custom_message = custom_message

    def get_phone_country(self):
        return self.__phone_country

    def set_phone_country(self, phone_country: str):
        self.__phone_country = phone_country

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def get_lock_email(self):
        return self.__lock_email

    def set_lock_email(self, lock_email: bool):
        self.__lock_email = lock_email

    def get_blank_email(self):
        return self.__blank_email

    def set_blank_email(self, blank_email: bool):
        self.__blank_email = blank_email

    def get_hide_email(self):
        return self.__hide_email

    def set_hide_email(self, hide_email: bool):
        self.__hide_email = hide_email

    def get_lock_phone(self):
        return self.__lock_phone

    def set_lock_phone(self, lock_phone: bool):
        self.__lock_phone = lock_phone

    def get_blank_phone(self):
        return self.__blank_phone

    def set_blank_phone(self, blank_phone: bool):
        self.__blank_phone = blank_phone

    def get_hide_phone(self):
        return self.__hide_phone

    def set_hide_phone(self, hide_phone: bool):
        self.__hide_phone = hide_phone

    def get_lock_name(self):
        return self.__lock_name

    def set_lock_name(self, lock_name: bool):
        self.__lock_name = lock_name

    def get_require_selfie_photo(self):
        return self.__require_selfie_photo

    def set_require_selfie_photo(self, require_selfie_photo: bool):
        self.__require_selfie_photo = require_selfie_photo

    def get_selfie_validation_type(self):
        return self.__selfie_validation_type

    def set_selfie_validation_type(self, selfie_validation_type: str):
        self.__selfie_validation_type = selfie_validation_type

    def get_qualification(self):
        return self.__qualification

    def set_qualification(self, qualification: str):
        self.__qualification = qualification

    def get_external_id(self):
        return self.__external_id

    def set_external_id(self, external_id: str):
        self.__external_id = external_id

    def get_redirect_link(self):
        return self.__redirect_link

    def set_redirect_link(self, redirect_link: str):
        self.__redirect_link = redirect_link

    def get_sign_url(self):
        return self.__sign_url

    def set_sign_url(self, sign_url: str):
        self.__sign_url = sign_url

    def get_token(self):
        return self.__token

    def set_token(self, token: str):
        self.__token = token

    def get_status(self):
        return self.__status

    def set_status(self, status: str):
        self.__status = status

    def get_times_viewed(self):
        return self.__times_viewed

    def set_times_viewed(self, times_viewed: int):
        self.__times_viewed = times_viewed

    def get_last_view_at(self):
        return self.__last_view_at

    def set_last_view_at(self, last_view_at: str):
        self.__last_view_at = last_view_at

    def get_signed_at(self):
        return self.__signed_at

    def set_signed_at(self, signed_at: str):
        self.__signed_at = signed_at

    def get_geo_latitude(self):
        return self.__geo_latitude

    def set_geo_latitude(self, geo_latitude: str):
        self.__geo_latitude = geo_latitude

    def get_geo_longitude(self):
        return self.__geo_longitude

    def set_geo_longitude(self, geo_longitude: str):
        self.__geo_longitude = geo_longitude

    def get_signature_image(self):
        return self.__signature_image

    def set_signature_image(self, signature_image: str):
        self.__signature_image = signature_image

    def get_visto_image(self):
        return self.__visto_image

    def set_visto_image(self, visto_image: str):
        self.__visto_image = visto_image

    def get_document_photo_url(self):
        return self.__document_photo_url

    def set_document_photo_url(self, document_photo_url: str):
        self.__document_photo_url = document_photo_url

    def get_document_verse_photo_url(self):
        return self.__document_verse_photo_url

    def set_document_verse_photo_url(self, document_verse_photo_url: str):
        self.__document_verse_photo_url = document_verse_photo_url

    def get_selfie_photo_url(self):
        return self.__selfie_photo_url

    def set_selfie_photo_url(self, selfie_photo_url: str):
        self.__selfie_photo_url = selfie_photo_url

    def get_selfie_photo_url2(self):
        return self.__selfie_photo_url2

    def set_selfie_photo_url2(self, selfie_photo_url2: str):
        self.__selfie_photo_url2 = selfie_photo_url2

    def get_send_via(self):
        return self.__send_via

    def set_send_via(self, send_via: str):
        self.__send_via = send_via

    def get_require_document_photo(self):
        return self.__require_document_photo

    def set_require_document_photo(self, require_document_photo: str):
        self.__require_document_photo = require_document_photo