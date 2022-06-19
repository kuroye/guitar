from django.urls import path
from .views import song
urlpatterns = [
    path('', song, name='song')
]