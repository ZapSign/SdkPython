class SignBatch:
    __user_token: str = ''
    __signer_tokens: [str] = []

    def get_user_token(self):
        return self.__user_token

    def set_user_token(self, user_token: str):
        self.__user_token = user_token

    def get_signer_tokens(self):
        return self.__signer_tokens

    def set_signer_tokens(self, signer_tokens: [str]):
        self.__signer_tokens = signer_tokens