from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(CountryPage)
admin.site.register(StatePage)
admin.site.register(BlogCategory)
admin.site.register(Post)
admin.site.register(ContactUs)
@admin.register(City)
class Cities(ImportExportModelAdmin):
    pass
@admin.register(AddListingRequest)
class AddListingRequest(ImportExportModelAdmin):
    pass
@admin.register(BusinessDetails)
class Business_details(ImportExportModelAdmin):
    pass
