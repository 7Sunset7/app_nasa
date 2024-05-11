from django.db import models
from filer.fields.image import FilerImageField


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = FilerImageField(on_delete=models.CASCADE, null=True, blank=True)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ["my_order"]

    def __str__(self):
        return self.title

