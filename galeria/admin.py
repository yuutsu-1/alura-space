from django.contrib import admin
from galeria.models import NASAImage


class NASAImageAdmin(admin.ModelAdmin):
    list_display = ("date", "title", "media_type")
    list_display_links = ("date", "title")
    search_fields = ("title",)
    list_filter = ("media_type",)
    
admin.site.register(NASAImage, NASAImageAdmin)

