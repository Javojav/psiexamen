"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path


# nuevo import
from application import views as application_views;

from django.urls import include
from rest_framework import routers
router = routers.DefaultRouter()

router.register('canal', application_views.CanalViewSet)
router.register('usuario', application_views.UsuarioViewSet)
router.register('suscripcion', application_views.SuscripcionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # imporatante meterle 1 barra al final (como si fuese 1 siri haciendo barra)
    path('application/canal/<int:pk>/', application_views.CanalDetailView.as_view(), name='canal-detail'),

    path('api/', include(router.urls)),
]
