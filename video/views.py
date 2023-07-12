from django.shortcuts import render
from .models import Video

def videos(request):
    videos = Video.objects.all()
    return render(request, 'video/videos.html', {'videos': videos,})
