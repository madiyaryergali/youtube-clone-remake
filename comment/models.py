from django.db import models
from django.contrib.auth.models import User
from video.models import Video

class Comment(models.Model):
    comment_text= models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)

