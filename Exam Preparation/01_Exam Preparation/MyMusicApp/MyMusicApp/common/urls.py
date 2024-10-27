from django.urls import path
from MyMusicApp.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]