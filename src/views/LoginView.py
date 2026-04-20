import flet as ft
def Loginview(page: ft.Page, auth_controller):
    email_input = ft.TextField(
        label="Correo elecronico", 
        width=350,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL
    )