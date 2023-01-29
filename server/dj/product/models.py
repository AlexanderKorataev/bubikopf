from io import BytesIO
from PIL import Image

from django.db import models
from django.core.files import File


class Product(models.Model):

    ru_name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    slug = models.SlugField(default=f'lesson_')
    ru_description = models.TextField(blank=True, null=True)
    en_description = models.TextField(blank=True, null=True)
    ru_price = models.DecimalField(max_digits=10, decimal_places=0)
    en_price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    video_file_id = models.CharField(max_length=15, blank=True, null=False)

    video_duration = models.CharField(max_length=4, blank=True, null=False)

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.ru_name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url # type: ignore
            
        elif self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()

            return 'http://127.0.0.1:8000' + self.thumbnail.url # type: ignore
    
        else:
            return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)

        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Products(models.Model): # ?
    pass