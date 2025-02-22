from django.urls import path
from .views import *

urlpatterns = [
    path('', ping, name='ping'),
    path('logo/', logo_view, name='logo'),
    path('slider/', slider_list_view, name='slider-list'),
    path('menu/', menu_view, name='menu-list'),
]