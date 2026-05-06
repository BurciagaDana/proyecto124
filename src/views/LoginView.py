import flet as ft
from controllers.UserController import UserController
from models.databaseModel import Database   # 👈 Importa la clase Database

def main(page: ft.Page):
    page.title = "Iniciar Sesión Bv"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    user_ctrl = UserController()

    nombre = ft.TextField(label="Nombre completo", width=280, prefix_icon=ft.Icons.PERSON)
    email = ft.TextField(label="Correo electrónico", width=280, prefix_icon=ft.Icons.ALTERNATE_EMAIL)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=280, prefix_icon=ft.Icons.PASSWORD)
    confirmar = ft.TextField(label="Confirmar contraseña", password=True, can_reveal_password=True, width=280, prefix_icon=ft.Icons.PASSWORD)

    mensaje = ft.Text("")
    contenido_central = ft.Column(alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)

    def mostrar_login():
        page.clean()
        sesion = ft.Container(
            width=350,
            padding=30,
            border_radius=10,
            bgcolor="white",
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    ft.Text("Inicio de sesión", size=24, weight=ft.FontWeight.BOLD),
                    email,
                    password,
                    ft.ElevatedButton("Iniciar sesión", width=280, on_click=iniciar_sesion),
                    ft.Divider(),
                    ft.Text("Registro de usuario", size=20, weight=ft.FontWeight.BOLD),
                    nombre,
                    email,
                    password,
                    confirmar,
                    ft.ElevatedButton("Registrarse", width=280, on_click=registrar_usuario),
                    mensaje
                ]
            )
        )
        page.add(sesion)

    def pagina_principal(nombre_usuario):
        page.clean()
        barra_nav = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ElevatedButton("Inicio", on_click=mostrar_inicio),
                ft.Container(expand=True),
                ft.ElevatedButton("Perfil", on_click=mostrar_perfil)
            ]
        )
        boton_salida = ft.ElevatedButton("Salir", icon=ft.Icons.LOGOUT, on_click=lambda e: mostrar_login())
        mostrar_inicio(None)
        page.add(ft.Column(expand=True, controls=[barra_nav, contenido_central, ft.Row(controls=[boton_salida], alignment=ft.MainAxisAlignment.START)]))

    def mostrar_inicio(e):
        contenido_central.controls = [ft.Text("Bienvenido al sistema", size=30, weight=ft.FontWeight.BOLD)]
        page.update()

    def mostrar_perfil(e):
        contenido_central.controls = [
            ft.Text("Perfil del usuario", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(f"Email: {email.value}")
        ]
        page.update()

    def iniciar_sesion(e):
        success, msg = user_ctrl.iniciar_sesion(email.value, password.value)
        if success:
            mensaje.value = msg
            pagina_principal(nombre.value)
        else:
            mensaje.value = msg
            mensaje.color = "red"
        page.update()

    def registrar_usuario(e):
        if password.value != confirmar.value:
            mensaje.value = "Las contraseñas no coinciden"
            mensaje.color = "red"
        else:
            success, msg = user_ctrl.registrar_usuario(nombre.value, email.value, password.value)
            mensaje.value = msg
            mensaje.color = "green" if success else "red"
        page.update()

    mostrar_login()

# 👇 Aquí llamamos a la creación de tablas ANTES de arrancar la app
Database.create_tables()

ft.app(target=main)
