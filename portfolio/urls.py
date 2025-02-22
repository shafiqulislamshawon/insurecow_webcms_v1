from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', category_view, name='category-list'),  # List of all categories
    path('category/<uuid:category_id>/portfolios/', category_portfolio_view, name='category-portfolio-list'),
    path('portfolios/<uuid:category_id>/', portfolio_view, name='portfolio-list'),  # List of active portfolios by category
    path('portfolio/<uuid:portfolio_id>/', portfolio_details_view, name='portfolio-details'),  # Portfolio details by ID
]