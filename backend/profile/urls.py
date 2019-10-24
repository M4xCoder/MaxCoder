from django.urls import path, include
from .views import ProfilePage, LicensePage



urlpatterns = [
    path('profile/', ProfilePage.as_view(), name="profile"),
    path('license/', LicensePage.as_view(), name="license"),
]
