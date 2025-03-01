from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

from .models import *

# Register your models here.
admin.site.register(Category)
# admin.site.register(Portfolio)

class PortfolioResource(ModelResource):
    class Meta:
        model = Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(ImportExportModelAdmin):
    resource_class = PortfolioResource