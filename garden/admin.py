from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Turlar,Gul

admin.site.register(Turlar)

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','created', 'turi', 'published', 'get_image')
    list_display_links = ('name', 'pk')
    list_editable = ('published', 'turi')
    list_filter = ('turi', 'published')
    search_fields = ('pk', 'name', 'info')
    list_per_page = 10

    def get_image(self, gul):
        if gul.photo:
            return mark_safe(f'<img src="{gul.photo.url}" width="150px">')
        else:
            return '-'

    get_image.short_description = "Rasmi"
admin.site.register(Gul, PostAdmin)
