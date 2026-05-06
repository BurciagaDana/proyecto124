from models.TareaModel import TareaModel

class TareaController:
    def __init__(self):
        self.model = TareaModel()

    def obtener_lista(self, id_usuario):
        return self.model.listar_por_usuario(id_usuario)

    def guardar_nueva(self, id_usuario, titulo, desc, prio, clas):
        if not titulo:
            return False, "El título es obligatorio"
        
        try:
            self.model.crear(id_usuario, titulo, desc, prio, clas)
            return True, "Tarea creada exitosamente"
        except Exception as e:
            return False, f"Error al crear tarea: {e}"
