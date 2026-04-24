import flet as ft

def main(page: ft.Page):
    page.title = "Iniciar Sesión Bv"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Datos de prueba
    correo_prueba = "player124@gmail.com"
    contraseña_prueba = "1020"

    # Campos de login
    correo = ft.TextField(
        label="Correo electrónico",
        width=280,
        prefix_icon=ft.Icons.ALTERNATE_EMAIL
    )
    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=280,
        prefix_icon=ft.Icons.PASSWORD
    )

    mensaje = ft.Text("")

    # Contenedor dinámico para el contenido central
    contenido_central = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    # Función para mostrar login
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
                    correo,
                    contraseña,
                    ft.ElevatedButton(
                        "Iniciar sesión",
                        width=280,
                        on_click=iniciar_sesion,
                        style=ft.ButtonStyle(
                            bgcolor={
                                ft.ControlState.DEFAULT: "#4C7AAF",
                                ft.ControlState.HOVERED: "#3a4498"
                            },
                            color="white"
                        )
                    ),
                    mensaje
                ]
            )
        )
        page.add(sesion)

    # Función para mostrar página principal
    def pagina_principal():
        page.clean()

        # Barra de navegación con Inicio y Perfil
        barra_nav = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ElevatedButton("Inicio", on_click=mostrar_inicio),
                ft.Container(expand=True),  # espacio flexible
                ft.ElevatedButton("Perfil", on_click=mostrar_perfil)
            ]
        )

        # Botón de salida
        boton_salida = ft.ElevatedButton(
            "Salir",
            icon=ft.Icons.LOGOUT,
            on_click=lambda e: mostrar_login()
        )

        # Contenido central inicial
        mostrar_inicio(None)

        # Layout principal
        page.add(
            ft.Column(
                expand=True,
                controls=[
                    barra_nav,
                    contenido_central,
                    ft.Row(
                        controls=[boton_salida],
                        alignment=ft.MainAxisAlignment.START
                    )
                ]
            )
        )

    # Funciones para cambiar contenido central
    def mostrar_inicio(e):
        contenido_central.controls = [
            ft.Text("Bienvenido al sistema", size=30, weight=ft.FontWeight.BOLD)
        ]
        page.update()

    def mostrar_perfil(e):
        contenido_central.controls = [
            ft.Text("Perfil del usuario", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(f"Correo: {correo.value}")
        ]
        page.update()

    # Validación login
    def iniciar_sesion(e):
        if correo.value == correo_prueba and contraseña.value == contraseña_prueba:
            pagina_principal()
        else:
            mensaje.value = "Correo o contraseña incorrectos"
            mensaje.color = "red"
            page.update()

    # Mostrar login al inicio
    mostrar_login()

ft.app(target=main)
