from django.urls import path
from . import views
from .views import user_list, edit_user, document_approval


urlpatterns = [
    path('login_success/', views.login_success, name='login_success'),
    path('home/', views.home, name='home'),
    path('checa-documentos/', views.checa_documents, name="checa_documentos"),
    path('alteracao_cadastral/', user_list, name='alteracao_cadastral'),
    path('<int:pk>/edit/', edit_user, name='edit_user'),
    path('document_approval/', document_approval, name="document_approval"),
    path('document_preview/<int:document_id>/', views.document_preview, name='document_preview'),
    path('authors/', views.author_list, name='author_list'),
    path('documents/<int:author_id>/', views.document_list, name='document_list'),
    path('documents/<int:document_id>/change_status/', views.change_status, name='change_status'),
    path('documents/<int:document_id>/delete/', views.delete_document, name='delete_document'),
]
