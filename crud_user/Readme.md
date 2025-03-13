📌 Proyecto Django con API y Pruebas Automatizadas

📖 Descripción

Este es un proyecto en Django que implementa un CRUD de usuarios con una API REST y pruebas automatizadas.
El objetivo es gestionar usuarios mediante una interfaz web y exponer los datos a través de una API para integraciones con otras aplicaciones.

🚀 Tecnologías utilizadas

Django 5.1.7 - Framework web principal.

Django REST Framework (DRF) - Para la construcción de la API REST.

SQLite (por defecto) - Base de datos.

Pytest & Pytest-Django - Para pruebas automatizadas.

Faker - Para generar datos de prueba.

📂 Estructura del Proyecto

web_user/
│-- crud_user/              # Aplicación principal del CRUD
│   ├── migrations/         # Migraciones de la base de datos
│   ├── tests/              # Pruebas automatizadas
│   │   ├── test_forms.py   # Pruebas de formularios
│   │   ├── test_views.py   # Pruebas de vistas
│   │   ├── test_api.py     # Pruebas de la API
│   ├── models.py           # Modelos de la base de datos
│   ├── views.py            # Lógica de vistas y API
│   ├── urls.py             # Rutas del CRUD y API
│   ├── serializers.py      # Serializadores para la API
│-- web_user/
│   ├── settings.py         # Configuración del proyecto Django
│   ├── urls.py             # Rutas globales del proyecto
│-- manage.py               # Comando principal de Django

🛠 Instalación y Configuración

1️⃣ Clonar el repositorio

git clone https://github.com/tu_usuario/tu_proyecto.git
cd tu_proyecto

2️⃣ Crear y activar un entorno virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

3️⃣ Instalar dependencias

pip install -r requirements.txt

4️⃣ Aplicar migraciones y ejecutar el servidor

python manage.py migrate
python manage.py runserver

🌐 API REST

El proyecto expone una API REST para gestionar los usuarios.

🔹 Endpoints disponibles

Método

URL

Descripción

GET

/api/usuarios/

Listar todos los usuarios

POST

/api/usuarios/

Crear un nuevo usuario

GET

/api/usuarios/{id}/

Obtener un usuario por ID

PUT

/api/usuarios/{id}/

Actualizar un usuario por ID

DELETE

/api/usuarios/{id}/

Eliminar un usuario por ID

📌 Ejemplo de petición con curl

🔹 Crear un usuario:

curl -X POST http://127.0.0.1:8000/api/usuarios/ \  
     -H "Content-Type: application/json" \  
     -d '{"nombre": "Juan Pérez", "direccion": "Calle 123", "telefono": "1234567", "correo": "juan@example.com", "genero": "M", "edad": 30}'

🔹 Listar usuarios:

curl -X GET http://127.0.0.1:8000/api/usuarios/

🧪 Pruebas Automatizadas

El proyecto incluye pruebas automatizadas con pytest.

🔹 Ejecutar todas las pruebas:

python -m pytest

🔹 Tipos de pruebas incluidas:

Pruebas unitarias: Verifican el funcionamiento de los formularios y modelos.

Pruebas de integración: Validan la comunicación entre la API y la base de datos.

Pruebas funcionales: Aseguran que las vistas y flujos de usuario operan correctamente.

🎯 Próximos pasos

Mejorar la seguridad de la API.

Agregar autenticación y permisos.

Implementar pruebas de carga y rendimiento.


📜 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo libremente respetando los términos de la licencia.