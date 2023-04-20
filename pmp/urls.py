from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import document_approval_form

urlpatterns = [
    path('', RedirectView.as_view(url='accounts/login/')),
    path('fileupload/', views.fileupload, name='fileupload'),  # Temporário
    path('document_approval_form', document_approval_form, name='document_approval_form')
]
