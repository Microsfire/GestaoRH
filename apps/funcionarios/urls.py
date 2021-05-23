from django.urls import path
from .views import FuncionarioList


urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionarios'),
]