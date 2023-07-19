from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.index, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.log_out, name='logout'),
]
