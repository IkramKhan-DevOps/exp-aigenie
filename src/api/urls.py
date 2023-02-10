from django.urls import re_path, path

from src.api.views import (
    OpenAIChatAPi, PurchaseRetrieveAPIView, PurchaseListAPIView, PurchaseCreateAPIView,
    PackageListAPIView, ProfileRetrieveView
)

app_name = "api"
urlpatterns = [
    re_path('chat-with-ai/', OpenAIChatAPi.as_view(), name="open-ai"),

    path('purchase/', PurchaseListAPIView.as_view(), name="purchase"),
    path('purchase/add/', PurchaseCreateAPIView.as_view(), name="purchase-add"),
    path('purchase/<int:pk>/', PurchaseRetrieveAPIView.as_view(), name="purchase-detail"),
    path('who-am-i/', ProfileRetrieveView.as_view(), name="profile-details"),

    path('package/', PackageListAPIView.as_view(), name="package"),
]
