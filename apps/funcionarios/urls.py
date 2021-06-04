from django.urls import path
from .views import (
    FuncionarioList,
    FuncionarioEdit, FuncionarioDelite,
    FuncionarioNovo
)


urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionarios'),
    path('new/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelite.as_view(), name='delete_funcionario'),

]