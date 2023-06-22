from django.urls import path
from . import views
from .views import signup


urlpatterns = [
    path('registrar/', views.signup, name='account_signup'),
]
