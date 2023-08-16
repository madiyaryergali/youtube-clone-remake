from django.shortcuts import render, get_object_or_404
from video.models import Video
from .models import Channel
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class VideoListView(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'channel/channel_home.html' 

    def get_queryset(self):
        user_channel = self.request.user.channel
        return Video.objects.filter(channel_id=user_channel)

def channel_detail(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    videos = Video.objects.filter(channel_id=channel)
    return render(request, 'channel/channel_detail.html', {'channel': channel, 'videos': videos})
