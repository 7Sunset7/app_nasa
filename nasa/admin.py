from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Image
from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer

@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):

    def image_tag(self, obj):
        thumbnail_url = get_thumbnailer(obj.image)['my_preview_1'].url
        return mark_safe(f'<img src="{thumbnail_url}" />')

    image_tag.short_description = 'Изображение'

    list_display = ('title', 'image_tag', 'my_order')
