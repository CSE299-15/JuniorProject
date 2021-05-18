from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('payments/', include('payment.urls', namespace='payments')),
    path('chats/', include('chats.urls', namespace='chats')),
]