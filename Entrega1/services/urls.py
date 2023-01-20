from django.urls import path
from services.views import create_transport




urlpatterns = [
    path('create-transport/', create_transport),
]