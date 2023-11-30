from src.body.create_by import CreateBy

class CreateByBuilder:
    create_by: CreateBy

    def __init__(self):
        self.create_by = CreateBy()

    def with_email(self, email: str):
        self.create_by.set_email(email)
        return self

    def build(self):
        return self.create_by