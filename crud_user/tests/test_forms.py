import pytest
from crud_user.forms import UsuarioForm

@pytest.mark.django_db
def test_usuario_form_valido():
    """Prueba si el formulario es válido con datos correctos."""
    form_data = {
        "nombre": "Juan Pérez",
        "direccion": "Av. Siempre Viva 742",
        "telefono": "123456789",
        "correo": "juan@example.com",
        "genero": "M",
        "edad": 30
    }
    form = UsuarioForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_usuario_form_invalido():
    """Prueba si el formulario es inválido con datos incorrectos."""
    form_data = {
        "nombre": "",  # Nombre vacío
        "direccion": "Av. Siempre Viva 742",
        "telefono": "abc123",  # Teléfono inválido
        "correo": "correo-invalido",  # Correo inválido
        "genero": "X",  # Género no válido
        "edad": -5  # Edad inválida
    }
    form = UsuarioForm(data=form_data)
    assert form.is_valid() is False
