import flet as 
def LoginView(page, auth_controller):
    email_input = ft.TextField(label= "Correo electronico", width=350, border_radius=10)
    pass_input = ft.TextFiel(label= "Contraseña", password=True, can_reveal_password= True, width=350, border_radius=10)
    
    def login_click():
        user, msg = auth_controller.login(email_input.value,pass_input.value)
        if user: 
            page.session.set("user", user) #guardamos la sesion
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
            
        
    retur ft.view("/", [
        ft.AppBAr(title=ft.Text("SIGE - Login"), bgcolor= ft.Colors.BLUE_GREY_900, color="white"),
        ft.Column([
            ft.Icon(ft.Icons.LOCK_PERSON, size=50, color=ft.Colors.BLUE),
            ft.Text("Acceso al sistema", size=24, weight="bold"), 
            email_input,
            pass_input,
            ft.ElevatedButton("Entrar", on_ click=login_click, width=350),
            ft.TextButton("Crear una cuenta nueva", on_click=lambda _: page.go("/ "))
            
            
        ])
    ])            