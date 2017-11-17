from django.conf.urls import url
from django.contrib import admin
from accounts.views import get_index, logout, login, register, profile

urlpatterns = [
    url(r"^logout$", logout, name="logout"),
    url(r"^login$", login, name="login"),
    url(r"^register$", register, name="register"),
    url(r"^profile$", profile, name="profile"),
]

