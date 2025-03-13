import pytest
from django.urls import reverse
from crud_user.models import Usuario

@pytest.mark.django_db
def test_lista_usuarios(client):
    """Verifica que la vista de lista de usuarios cargue correctamente"""
    response = client.get(reverse('lista_usuarios'))
    assert response.status_code == 200
    assert b'Lista de Usuarios' in response.content  # Verifica si el título está en el HTML

@pytest.mark.django_db
def test_crear_usuario_get(client):
    """Verifica que la vista de creación de usuario cargue correctamente"""
    response = client.get(reverse('crear_usuario'))
    assert response.status_code == 200
    assert b'Formulario de Usuario' in response.content

@pytest.mark.django_db
def test_crear_usuario_post(client):
    """Prueba la creación de un usuario con datos válidos"""
    data = {
        "nombre": "Juan Pérez",
        "direccion": "Calle 123",
        "telefono": "555-5555",
        "correo": "juan@example.com",
        "genero": "M",
        "edad": 30
    }
    response = client.post(reverse('crear_usuario'), data)
    assert response.status_code == 302  # Redirige tras creación
    assert Usuario.objects.filter(correo="juan@example.com").exists()

@pytest.mark.django_db
def test_editar_usuario_get(client):
    """Verifica que la vista de edición de usuario cargue correctamente"""
    usuario = Usuario.objects.create(nombre="María Gómez", direccion="Av. Principal", telefono="444-4444",
                                     correo="maria@example.com", genero="F", edad=25)
    response = client.get(reverse('editar_usuario', args=[usuario.id]))
    assert response.status_code == 200
    assert b'Formulario de Usuario' in response.content

@pytest.mark.django_db
def test_editar_usuario_post(client):
    """Prueba la actualización de un usuario existente"""
    usuario = Usuario.objects.create(nombre="Carlos López", direccion="Calle 789", telefono="333-3333",
                                     correo="carlos@example.com", genero="M", edad=40)
    data = {
        "nombre": "Carlos López Editado",
        "direccion": "Calle 789",
        "telefono": "333-3333",
        "correo": "carlos@example.com",
        "genero": "M",
        "edad": 41
    }
    response = client.post(reverse('editar_usuario', args=[usuario.id]), data)
    usuario.refresh_from_db()
    assert response.status_code == 302
    assert usuario.nombre == "Carlos López Editado"
    assert usuario.edad == 41

@pytest.mark.django_db
def test_eliminar_usuario(client):
    """Prueba la eliminación de un usuario"""
    usuario = Usuario.objects.create(nombre="Pedro Jiménez", direccion="Calle X", telefono="222-2222",
                                     correo="pedro@example.com", genero="M", edad=35)
    response = client.post(reverse('eliminar_usuario', args=[usuario.id]))
    assert response.status_code == 302
    assert not Usuario.objects.filter(id=usuario.id).exists()
