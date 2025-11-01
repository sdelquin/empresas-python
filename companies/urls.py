from django.urls import path

from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.index, name='index'),
    path('listado/', views.company_list, name='company-list'),
]
