from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Image
from adminsortable2.admin import SortableAdminMixin

@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')

    image_tag.short_description = 'Image'

    list_display = ('title', 'image_tag', 'my_order')
