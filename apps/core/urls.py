from django.urls import path
from apps.core import views

urlpatterns = [
    path('',views.home, name='home'),
    path('celery/', views.celery, name='celery'),
]