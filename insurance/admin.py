from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(InsuranceType)
admin.site.register(UserSubmission)
admin.site.register(DynamicFormField)
admin.site.register(DynamicFormResponse)