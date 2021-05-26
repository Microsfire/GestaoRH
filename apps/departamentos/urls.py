from django.urls import path
from .views import (
    DepartamentoList,
    DepartamentoCreate,
    DepartamentoEdit,
    DepartamentoDelete
)

urlpatterns = [
    path('list/', DepartamentoList.as_view(),name='list_deparatamentos'),
    path('novo/', DepartamentoCreate.as_view(),name='create_deparatamentos'),
    path('editar/<int:pk>', DepartamentoEdit.as_view(),name='update_departamentos'),
    path('deletar/<int:pk>', DepartamentoDelete.as_view(),name='delete_departamentos'),
]