from django.contrib import admin
from yushen.models import Part

# Register your models here.

class PartAdmin(admin.ModelAdmin):
    list_display = ('identifier','type','elevator','visibility')
    list_filter = ['type',  'elevator', 'visibility']
    search_fields = ['identifier']
admin.site.register(Part, PartAdmin)
