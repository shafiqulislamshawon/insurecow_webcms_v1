
from django.urls import path
from .views import *

urlpatterns = [
    path('insurance-types/', insurance_types_view, name='insurance_types_view'),
    path('insurance-types/<int:insurance_type_id>/form/', dynamic_form_view, name='dynamic_form_view'),
    path('submit-form/', form_submission_view, name='form_submission_view'),
]
