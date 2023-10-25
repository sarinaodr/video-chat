from django.urls import path

from .views import lobby , room

urlpatterns = [
    path('' , lobby , name='lobby'),
    path('room/' , room , name='room'),
]
