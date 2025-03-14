from locust import HttpUser, task, between

class UsuarioSimulado(HttpUser):
    wait_time = between(1, 3)  # Tiempo de espera entre solicitudes

    @task
    def cargar_lista_usuarios(self):
        """Prueba la carga de la lista de usuarios"""
        self.client.get("/crud/")  # Ajusta la URL según tu app

    @task
    def crear_usuario(self):
        """Prueba la creación de un usuario"""
        self.client.post("/crud/nuevo/", {
            "nombre": "Prueba Locust",
            "direccion": "Calle Test",
            "telefono": "987654321",
            "correo": "test@example.com",
            "genero": "M",
            "edad": "25"
        })
