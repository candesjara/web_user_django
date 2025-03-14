from django.test import TestCase
from django.db.utils import IntegrityError
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
        self.assertEqual(str(usuario), "Juan Pérez")  # Asegura que __str__ funciona bien
        self.assertEqual(usuario.edad, 30)  # Comprobamos que la edad se guardó correctamente

    def test_correo_unico(self):
        """Verifica que no se puedan crear dos usuarios con el mismo correo."""
        Usuario.objects.create(
            nombre="Juan Pérez",
            direccion="Av. Principal 123",
            telefono="123456789",
            correo="juan@example.com",
            genero="M",
            edad=30
        )
        
        with self.assertRaises(IntegrityError):
            Usuario.objects.create(
                nombre="Ana Gómez",
                direccion="Calle 456",
                telefono="987654321",
                correo="juan@example.com",  # Misma dirección de correo
                genero="F",
                edad=25
            )

    def test_recuperar_usuario(self):
        """Verifica que los datos almacenados sean correctos al recuperarlos"""
        Usuario.objects.create(
            nombre="Juan Pérez",
            direccion="Calle 123",
            telefono="1234567",
            correo="juan@example.com",
            genero="M",
            edad=30
        )
        usuario_recuperado = Usuario.objects.get(correo="juan@example.com")

        self.assertEqual(usuario_recuperado.nombre, "Juan Pérez")
        self.assertEqual(usuario_recuperado.direccion, "Calle 123")
        self.assertEqual(usuario_recuperado.telefono, "1234567")
        self.assertEqual(usuario_recuperado.genero, "M")
        self.assertEqual(usuario_recuperado.edad, 30)
