from django.contrib import admin
from channel.models import Channel
from comment.models import Comment
from playlist.models import Playlist
from savedVideos.models import SavedVideos
from searchHistory.models import SearhHistory
from video.models import Video
from watchHistory.models import WatchHistory

admin.site.register(Channel)
admin.site.register(Comment)
admin.site.register(Playlist)
admin.site.register(SavedVideos)
admin.site.register(SearhHistory)
admin.site.register(Video)
admin.site.register(WatchHistory)
