from django.urls import path

from . import views

app_name = 'video'

urlpatterns =[
    path('', views.videos, name='videos'),
    path('new/', views.new, name ='new'),
    path('search/', views.search, name='search'),
    path('<int:pk>/', views.video_detail, name='video_detail'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
    #path('<int:pk>', views.detail, name='detail'),
    #path('<int:pk>/delete/', views.delete, name='delete'),
   # path('<int:pk>/edit/', views.edit, name='edit'),

] 