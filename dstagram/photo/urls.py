from django.urls import path
from django.views.generic.detail import DetailView
from .views import *
from .models import Photo

app_name = 'photo'
urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>/')
]