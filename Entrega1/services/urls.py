from django.urls import path
from services.views import create_transport, list_transports, services, create_activity, list_activities 




urlpatterns = [
    path('create-transport/', create_transport),
    path('list-transport/', list_transports),
    path('services/', services),
    path('create-activity/', create_activity),
    path('list-activities/', list_activities),
]