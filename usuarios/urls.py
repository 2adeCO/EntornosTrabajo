from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('registro/', views.registro, name='registro'),
    path('panel/', views.panel_usuario, name='panel'),
]
