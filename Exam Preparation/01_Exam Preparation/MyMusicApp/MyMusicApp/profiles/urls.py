from django.urls import path
from MyMusicApp.profiles import views

urlpatterns = [
    path('details/', views.ProfileDetailView.as_view(), name='profile-details'),
    path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]