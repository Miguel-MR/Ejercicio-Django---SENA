from rest_framework import serializers
from .models import Autor, Etiqueta, Articulo, Notificacion

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'email']

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ['id', 'nombre']

class ArticuloSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    autor_id = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all(), source='autor', write_only=True, required=False)
    etiquetas = EtiquetaSerializer(many=True, read_only=True)
    etiqueta_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Etiqueta.objects.all(), source='etiquetas', write_only=True, required=False)

    class Meta:
        model = Articulo
        fields = ['id', 'titulo', 'contenido', 'fecha_publicacion', 'esta_publicado', 'autor', 'autor_id', 'etiquetas', 'etiqueta_ids']

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = ['notificacion_id', 'nombre_notificacion', 'fecha_notificacion', 'categoria_notificacion', 'fecha_creacion', 'asunto', 'descripcion']