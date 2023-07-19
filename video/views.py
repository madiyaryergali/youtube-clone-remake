from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from django.contrib.auth.decorators import login_required
from .forms import NewVideoForm

def videos(request):
    videos = Video.objects.all()
    return render(request, 'video/videos.html', {'videos': videos,})

def detail(request, pk):
    item = get_object_or_404(Video, pk=pk)
    #related_items = Video.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        #'related_items': related_items,
    })

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
