from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Photo(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to='images', blank=False)
    upload_timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode(self):
        return self.title

    class Meta:
        ordering = ['title']

class Like(models.Model):
    user = models.ForeignKey(User)
    photo = models.ManyToManyField(Photo)
