from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelite,
    HoraExtraCreate,
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('new/', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('delitar/<int:pk>/', HoraExtraDelite.as_view(), name='delete_hora_extra'),

]
