import flet as ft


class Botao(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.text = text
        self.on_click = on_click