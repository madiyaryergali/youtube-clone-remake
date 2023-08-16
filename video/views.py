from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from django.contrib.auth.decorators import login_required
from .forms import NewVideoForm
from comment.models import Comment

from django.db.models import Q

def search(request):
    search_query = request.GET.get('search_query')

    if search_query:
        videos = Video.objects.filter(Q(name__icontains=search_query) | Q(channel_id__name__icontains=search_query))
    else:
        videos = Video.objects.all()

    context = {'videos': videos}
    return render(request, 'video/search.html', context)


def videos(request):
    videos = Video.objects.all()
    return render(request, 'video/videos.html', {'videos': videos,})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    comments = Comment.objects.filter(video_id=pk)
    return render(request, 'video/video_detail.html', {'video': video, 'comments':comments})

@login_required
def add_comment(request, pk):
    video = get_object_or_404(Video, pk=pk)

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        if comment_text:
            Comment.objects.create(video_id=video, comment_text=comment_text, user_id=request.user)

    return redirect('video:video_detail', pk=pk)


@login_required
def new(request):
    if request.method == "POST":
        form = NewVideoForm(request.POST, request.FILES)

        if form.is_valid():
            video = form.save(commit=False)
            video.channel_id = request.user.channel
            video.save()

            return redirect('video:videos')
    else:
        form = NewVideoForm()

    return render(request, 'video/form.html', {
        'form': form,
        'title': 'New item',
    })
