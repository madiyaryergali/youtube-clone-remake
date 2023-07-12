from django.db import models
from django.contrib.auth.models import User

class Channel(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='static/images_uploaded', null=True, blank=True)
    background = models.ImageField(upload_to='static/images_uploaded', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + ' : ' + self.name