from django.urls import path

from . import views

app_name = 'channel'

urlpatterns =[
    path('', views.VideoListView.as_view(), name='all_videos'),
    path('<int:pk>/', views.channel_detail, name='channel_detail'),
] 