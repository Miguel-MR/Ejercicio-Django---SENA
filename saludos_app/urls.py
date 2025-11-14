from django.urls import path
from . import views

urlpatterns = [
    # Cuando se visite la raíz de esta app, llama a la vista 'mostrar_saludo'
    path('', views.mostrar_saludo, name='saludo_principal'),
    path('ruta/', views.segunda_vista, name='saludo_secundario'),
    path('bio-sena/', views.bio_sena, name='bio_sena'),
]