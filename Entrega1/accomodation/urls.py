from django.urls import path

from accomodation.views import create_room, list_rooms



urlpatterns = [
    path('create-room/', create_room),
    path('list-rooms/', list_rooms),
]