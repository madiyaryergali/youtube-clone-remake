from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User

class Channel(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images_uploaded', null=True, blank=True)
    background = models.ImageField(upload_to='images_uploaded', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='channel')

    def __str__(self):
        return str(self.pk) + ' : ' + self.name
    
@receiver(post_save, sender=User)
def create_user_channel(sender, instance, created, **kwargs):
    
    if created:
        Channel.objects.create(user_id=instance, name=f"{instance.username}'s Channel")


post_save.connect(create_user_channel, sender=User)