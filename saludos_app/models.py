from django.db import models


# Autor: autor de artículos
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


# Etiqueta: etiquetas para los artículos (ManyToMany)
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


# Saludo: modelo existente (se mantiene)
class Saludo(models.Model):
    mensaje = models.CharField(max_length=100)

    def __str__(self):
        return self.mensaje


# Articulo: artículo de blog que ahora relaciona con Autor y Etiqueta
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    esta_publicado = models.BooleanField(default=True)

    # FK a Autor. Permitimos null=True para no romper migraciones existentes.
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='articulos',
        null=True,
        blank=True,
    )

    # Etiquetas (ManyToMany)
    etiquetas = models.ManyToManyField(Etiqueta, related_name='articulos', blank=True)

    def __str__(self):
        return self.titulo


# Notificacion: tabla para notificaciones del proyecto
class Notificacion(models.Model):
    notificacion_id = models.AutoField(primary_key=True)
    nombre_notificacion = models.CharField(max_length=100)
    fecha_notificacion = models.DateField()
    categoria_notificacion = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    asunto = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre_notificacion
