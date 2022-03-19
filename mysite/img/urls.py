from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
  
#comment
urlpatterns = [
    path('', avatarView, name = ''),
    path('success/', success, name = 'success'),
    path('display/', display, name = 'display'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)