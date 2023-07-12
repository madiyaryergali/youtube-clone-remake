from django.db import models
from django.contrib.auth.models import User
from video.models import Video

class SavedVideos(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    video = models.ManyToManyField(Video)
