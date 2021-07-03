from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelite,
    HoraExtraCreate,
    HoraExtraEditBase,
    UtilizouHoraExtra,
    ExportarParaCsv,
    ExportarExcel,
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('new/', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('editar-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
    path('delitar/<int:pk>/', HoraExtraDelite.as_view(), name='delete_hora_extra'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou-hora-extra'),
    path('exportar-csv/', ExportarParaCsv.as_view(), name='exportar_csv'),
    path('exportar-excel/', ExportarExcel.as_view(), name='exportar_excel'),

]