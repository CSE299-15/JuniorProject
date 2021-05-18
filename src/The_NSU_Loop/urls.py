from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view

urlpatterns = [
    path('', home_view, name='home-view'),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('jackpots/', include('jackpot.urls', namespace='jackpots')),
]