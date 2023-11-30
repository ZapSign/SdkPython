from src.body.signer.sign_batch import SignBatch

class SignBatchBuilder:
    signer_batch: SignBatch

    def __init__(self):
        self.signer_batch = SignBatch()

    def with_user_token(self, user_token: str):
        self.signer_batch.set_user_token(user_token)

    def with_signer_tokens(self, signer_tokens: [str]):
        self.with_signer_tokens(signer_tokens)
