from django.urls import path
from . import views

urlpatterns = [
    path('definir_contas/', views.definir_contas, name="definir_contas"),
    path('pagar_conta/<int:id>', views.pagar_conta, name="pagar_conta"),
    path('ver_contas/', views.ver_contas, name="ver_contas"),
]
