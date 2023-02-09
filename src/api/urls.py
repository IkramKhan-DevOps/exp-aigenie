from django.urls import include, re_path, path
from rest_framework import permissions

from src.api.views import (
    OpenAIChatAPi, PurchaseRetrieveAPIView, PurchaseListAPIView, PurchaseCreateAPIView, PackageListAPIView
)

app_name = "api"
# Api Urls
urlpatterns = [
    re_path('chat-with-ai/', OpenAIChatAPi.as_view(), name="open-ai"),

    path('purchase/', PurchaseListAPIView.as_view(), name="purchase"),
    path('purchase/add/', PurchaseCreateAPIView.as_view(), name="purchase-add"),
    path('purchase/<int:pk>/', PurchaseRetrieveAPIView.as_view(), name="purchase-detail"),

    path('package/', PackageListAPIView.as_view(), name="package"),
]
