from django.urls import path
from .views import *

urlpatterns = [
    path('', ping, name='ping'),
    path('logo/', logo_view, name='logo'),
    path('slider/', slider_list_view, name='slider-list'),
    path('testimonials/', testimonial_view, name='testimonials-list'),
    path('menu/', menu_view, name='menu-list'),

    path('contact-us/', contact_us_view, name='contact-us'),
    path('gallery/', get_gallery, name='get-gallery'),
    path('gallery/<int:gallery_id>/', get_gallery_item, name='get-gallery-item'), 

    path('faqs/', get_faqs, name='get-faqs'),

    path('base-categories/', category_view, name='category-list'),  # List of all categories
    path('base-category/<uuid:category_id>/base-cards/', category_portfolio_view, name='category-portfolio-list'),
    path('base-cards/', portfolio_view, name='portfolio-list'),  # List of active portfolios by category
    path('<uuid:portfolio_id>/', portfolio_details_view, name='portfolio-details'),  # Portfolio details by ID
]
