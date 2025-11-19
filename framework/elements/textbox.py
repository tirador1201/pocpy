from framework.base_elemen import BaseElement


class Textbox(BaseElement):

    @property
    def type_of(self) -> str:
        return "Textbox"
