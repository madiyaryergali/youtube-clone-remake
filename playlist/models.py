from django.db import models
from video.models import Video
from django.contrib.auth.models import User

class Playlist(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.ManyToManyField(Video)

    def __str__(self) -> str:
        return str(self.pk) + ' : ' + self.name
