from django.test import TestCase

# Create your tests here.
from crud_user.models import Usuario

class UsuarioModelTest(TestCase):
    def test_creacion_usuario(self):
        usuario = Usuario.objects.create(
            nombre="Juan Pérez",
            direccion="Av. Principal 123",
            telefono="123456789",
            correo="juan@example.com",
            genero="M",
            edad=30
        )
        self.assertEqual(str(usuario), "Juan Pérez")  # Asegurar que __str__ funciona bien
        self.assertEqual(usuario.edad, 30)  # Comprobamos que la edad se guardó correctamente
