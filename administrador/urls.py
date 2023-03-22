from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('checa-documentos/', views.checa_documents, name="checa_documentos"),
    path('login_success/', views.login_success, name='login_success')
]
