import flet as ft
from Assets.visual import Botao
from Packages.link_processing import link_processing



def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    campo_url = ft.TextField(hint_text="Insira URL", width= 450)
    botao_conv = Botao(text= "Converter", on_click= link_processing(campo_url.value))
    Caixa_de_Texto = ft.Row(controls=[campo_url,botao_conv],alignment=ft.MainAxisAlignment.CENTER)
    #page.controls.append(texto)
    page.controls.append(Caixa_de_Texto)
    page.update()


ft.app(main)