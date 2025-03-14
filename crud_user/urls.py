from django.urls import path, include
from .views import lista_usuarios, crear_usuario, editar_usuario, eliminar_usuario
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
urlpatterns = [
    path('', lista_usuarios, name='lista_usuarios'),
    path('nuevo/', crear_usuario, name='crear_usuario'),
    path('editar/<int:id>/', editar_usuario, name='editar_usuario'),
    path('eliminar/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
    path('api/', include(router.urls)),
]
