from django.urls import path
from .views import *

urlpatterns = [
    path('', ping, name='ping'),
    path('logo/', logo_view, name='logo'),
    path('slider/', slider_list_view, name='slider-list'),
    path('menu/', menu_view, name='menu-list'),

    path('contact-us/', contact_us_view, name='contact-us'),
    path('gallery/', get_gallery, name='get-gallery'),
    path('gallery/<int:gallery_id>/', get_gallery_item, name='get-gallery-item'), 

    path('faqs/', get_faqs, name='get-faqs'),
]