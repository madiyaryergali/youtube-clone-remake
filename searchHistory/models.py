from django.db import models
from django.contrib.auth.models import User

class SearhHistory(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    prompt = models.TextField()
    date = models.DateTimeField(auto_now_add=True)