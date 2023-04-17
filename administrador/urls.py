from django.urls import path
from . import views
from .views import user_list, edit_user


urlpatterns = [
    path('login_success/', views.login_success, name='login_success'),
    path('home/', views.home, name='home'),
    path('checa-documentos/', views.checa_documents, name="checa_documentos"),
    path('alteracao_cadastral/', user_list, name='alteracao_cadastral'),
    path('<int:pk>/edit/', edit_user, name='edit_user'),
]
