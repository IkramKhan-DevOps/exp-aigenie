from django.urls import include, re_path, path
from rest_framework import permissions

from src.api.views import OpenAIChatAPi

app_name = "api"
# Api Urls
urlpatterns = [
    re_path('chat-with-ai/', OpenAIChatAPi.as_view(), name="open-ai"),
]
