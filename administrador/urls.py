from django.urls import path
from . import views

urlpatterns = [
    path('login_success/', views.login_success, name='login_success'),
    path('home/', views.home, name='home'),
    path('checa-documentos/', views.checa_documents, name="checa_documentos")
]
