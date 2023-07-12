from django.db import models
from channel.models import Channel
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    video = models.FileField(upload_to='static/videos_uploaded', validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return str(self.pk) + ' : ' + self.name
