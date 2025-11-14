from django.contrib import admin
from .models import Saludo, Articulo, Autor, Etiqueta

# Registrar los modelos actuales para poder administrar CRUD desde el admin
admin.site.register(Saludo)
admin.site.register(Articulo)
admin.site.register(Autor)
admin.site.register(Etiqueta)