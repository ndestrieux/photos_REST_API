from django.db import models

from PIL import Image
from colorthief import ColorThief


# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False)
    album_id = models.IntegerField(blank=False, null=False)
    width = models.IntegerField()
    height = models.IntegerField()
    dominant_color = models.CharField(max_length=7)
    local_url = models.URLField(blank=False, null=False)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.width, self.height = self._get_image_size()
        self.dominant_color = self._get_dominant_color()
        super().save()

    def _get_image_size(self):
        return Image.open(self.local_url).size

    def _get_dominant_color(self):
        ct = ColorThief(self.local_url)
        [(r, g, b)] = ct.get_palette(color_count=2, quality=1)[:1]
        return f"#{r:02x}{g:02x}{b:02x}"

    def __str__(self):
        return self.title
