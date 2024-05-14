from django.db import models
from filer.fields.image import FilerImageField


class Image(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    image = FilerImageField(on_delete=models.CASCADE, null=True, blank=True)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок",
    )

    class Meta:
        ordering = ["my_order"]
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return self.title

