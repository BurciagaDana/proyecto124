import flet as ft
from controllers.UserController import AuthController
from controllers.TareaControllers import TareaController
from views.LoginView import LoginView
from views.DashboardView import DashboardView

def main(page: ft.Page):
    page.title = "Mi App"

    auth_controller = AuthController()
    tarea_controller = TareaController()

    # normalmente empiezas en login
    LoginView(page, auth_controller)

ft.app(target=main)
