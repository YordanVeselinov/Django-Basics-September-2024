from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyMusicApp.common.urls')),
    path('album/', include('MyMusicApp.albums.urls')),
    path('profile/', include('MyMusicApp.profiles.urls')),
]