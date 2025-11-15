from rest_framework import routers
from .views import AutorViewSet, EtiquetaViewSet, ArticuloViewSet, NotificacionViewSet

router = routers.DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'etiquetas', EtiquetaViewSet)
router.register(r'articulos', ArticuloViewSet)
router.register(r'notificaciones', NotificacionViewSet)

urlpatterns = router.urls
