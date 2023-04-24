
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('successful_cases', views.successful_cases, name='successful_cases')
]
