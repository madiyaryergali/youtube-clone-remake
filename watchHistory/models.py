from django.db import models
from django.contrib.auth.models import User
from video.models import Video

class WatchHistory(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    watch_date = models.DateTimeField(auto_now_add=True)
    video_id = models.ManyToManyField(Video)

