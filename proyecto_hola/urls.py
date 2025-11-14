"""
URL configuration for proyecto_hola project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

# Importaciones para Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Importación para obtener tokens
from rest_framework.authtoken import views as token_views

# Configuración de la info de Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Documentación de la API del Blog para el Taller de Django",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="profesor@django.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Rutas de la API para la app `saludos_app` (viewsets registrados)
    path('api/', include('saludos_app.api_urls')),
    
    # 2. Endpoint para obtener el Token (Login)
    path('api-token-auth/', token_views.obtain_auth_token),

    # 3. Rutas de Swagger (Documentación)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]