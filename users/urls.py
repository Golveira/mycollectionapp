from django.urls import path
from .views import register

urlpatterns = [
    path('', register, name='users_register'),
]
