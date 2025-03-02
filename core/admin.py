from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

from .models import *

# Register your models here.
admin.site.register(Logo)
admin.site.register(Slider)
admin.site.register(MenuItem)
admin.site.register(ContactUs)
admin.site.register(Testimonial)
admin.site.register(Gallery)
admin.site.register(FAQ)
admin.site.register(BaseCategory)


class BaseCardResource(ModelResource):
    class Meta:
        model = BaseCard

@admin.register(BaseCard)
class BaseCardAdmin(ImportExportModelAdmin):
    resource_class = BaseCardResource


