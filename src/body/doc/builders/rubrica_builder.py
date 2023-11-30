from src.body.doc.rubrica import Rubrica

class RubricaBuilder:
    rubrica: Rubrica

    def __init__(self):
        self.rubrica = Rubrica()

    def with_page(self, page: int):
        self.rubrica.set_page(page)
        return self

    def with_relative_position_bottom(self, relative_position_bottom: int):
        self.rubrica.set_relative_position_bottom(relative_position_bottom)
        return self

    def with_relative_position_left(self, relative_position_left: int):
        self.rubrica.set_relative_position_left(relative_position_left)
        return self

    def with_relative_size_x(self, relative_size_x: int):
        self.rubrica.set_relative_size_x(relative_size_x)
        return self

    def with_relative_size_y(self, relative_size_y: int):
        self.rubrica.set_relative_size_y(relative_size_y)
        return self

    def with_type(self, type: str):
        self.rubrica.set_type(type)
        return self

    def with_signer_token(self, signer_token: str):
        self.rubrica.set_signer_token(signer_token)
        return self

    def build(self):
        return self.rubrica