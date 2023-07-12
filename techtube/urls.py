from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', include('video.urls')),
    path('', include('base.urls')),
]
