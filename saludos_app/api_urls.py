from rest_framework import routers
from .views import AutorViewSet, EtiquetaViewSet, ArticuloViewSet

router = routers.DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'etiquetas', EtiquetaViewSet)
router.register(r'articulos', ArticuloViewSet)

urlpatterns = router.urls
