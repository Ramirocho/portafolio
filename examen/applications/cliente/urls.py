from django.contrib import admin
from django.urls import path
from . import views

app_name= "cliente_app"
urlpatterns = [
    path('listar_cliente/', views.ListAllCliente.as_view()),
    path('ver_cliente/<pk>', views.ClienteDetailView.as_view()),
    path('add_cliente/', views.ClienteCreateView.as_view()),
    path('success/', views.SuccessView.as_view(),name='correcto'),
    path('update-cliente/<pk>',views.ClienteUpdateView.as_view(),name='modificar_cliente')
]
