from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', RedirectView.as_view(url='home/')),
    path('fileupload/generic', views.fileupload, name='fileupload') #Temporário
]