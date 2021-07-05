"""gestaoRH URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from apps.core import views
from apps.funcionarios.api.views import FuncionarioViewSet
from apps.registro_hora_extra.api.views import RegistroHoraExtraViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/hora-extra', RegistroHoraExtraViewSet)


urlpatterns = [
    # apps.core
    path('', include('apps.core.urls')),

    # apps.funcionarios
    path('funcionarios/', include('apps.funcionarios.urls')),

    # login
    path('accounts/', include('django.contrib.auth.urls')),

    # apps.empresa
    path('empresa/', include('apps.empresas.urls')),

    # apps.departamentos
    path('departamentos/', include('apps.departamentos.urls')),

    # apps.documentos
    path('documento/', include('apps.documentos.urls')),

    # apps.horas_extras
    path('horas-extras/', include('apps.registro_hora_extra.urls')),

    #admin
    path('admin/', admin.site.urls),

    #django restframwork
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


